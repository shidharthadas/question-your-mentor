from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
import django.contrib.auth.password_validation as validators
from django.core import exceptions, serializers
from django.core.exceptions import ValidationError
from django.core.mail import send_mail #
from django.db import IntegrityError
from django.db.models import F
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view #
from rest_framework.exceptions import APIException #
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler #
from questionyourmentor.models import User, Query, Log
from .serializers import UserSerializer, QuerySerializer, LogSerializer
from .forms import * #


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = QuerySerializer

    def create(self, serializer):
        query = self.request.user
        creator = user if user.is_authenticated else None
        serializer.save(user=creator)


class userLogin(APIView): 
    # permission_classes = (IsAuthenticated, )
    def post(self, request):
        response = {'status':'failed', 'messages':[]}
        email = request.data['email']
        user_object = User.objects.filter(email=email).annotate(user_id=F('id')).values('user_id', 'password', 'first_name', 'role')
        if user_object:
            user = list(user_object)
            if check_password(request.data['password'], user[0]['password']):
                Log.objects.create(content_type='User logged in', user_id=user[0]['user_id'])           
                response['status'] = 'success'
                response['messages'].append('Logged in successfully.')
                response['email'] = email
                user[0].pop("password")
                response.update(user[0])
            else:
                response['messages'].append('Email or password did not match.')
        else:
            response['messages'].append('Email or password did not match.')
        return Response(response)


class userSendingQuery(APIView): 
    # permission_classes = (IsAuthenticated, )
    def post(self, request):
        response = {'status':'failed', 'messages':[]}
        user_object = User.objects.filter(id=request.data['user']).values('role')
        mentor_object = User.objects.filter(id=request.data['mentor_user_id']).values('role')
        if user_object and mentor_object:
            user = list(user_object)
            mentor = list(mentor_object)
            if 'User' == user[0]['role'] and 'Mentor' == mentor[0]['role']:
                if request.FILES.get('attachment', False):
                    form = QueryFormWithAttachment(request.data, request.FILES)
                else:
                    form = QueryFormWithoutAttachment(request.data)
                if form.is_valid():
                    form.save()
                    Log.objects.create(content_type='User sent a query', user_id=request.data['user'])
                    response['status'] = 'success'
                    response['messages'].append('Your query has been sent.')
                else:
                    response['messages'].append('Message field cannot be left empty.')
            else:
                response['messages'].append('Only role with User can sent query to Mentor.')
        else:
            response['messages'].append('User or Mentor does not exists.')
        return Response(response)


class viewQuery(APIView): 
    # permission_classes = (IsAuthenticated, )
    def post(self, request):
        response = {'status':'failed', 'messages':[]}
        user_object = User.objects.filter(id=request.data['user_id']).values('role')
        if user_object:
            user = list(user_object)
            if 'User' == user[0]['role']:
                query_object = Query.objects.filter(user_id=request.data['user_id']).annotate(query_id=F('id')).values('query_id', 'query_message', 'attachment', 'mentor_user_id', 'response_message')
                query = list(query_object)
                if len(query) == 0:
                    response['messages'].append('You don\'t have any query.')
                Log.objects.create(content_type='User viewed all query', user_id=request.data['user_id'])
                response['status'] = 'success'
                response['queries'] = query
            elif 'Mentor' == user[0]['role']:
                query_object = Query.objects.filter(mentor_user_id=request.data['user_id']).annotate(query_id=F('id')).values('query_id', 'user_id', 'query_message', 'attachment', 'response_message')
                query = list(query_object)
                if len(query) == 0:
                    response['messages'].append('You don\'t have any query from Role:User.')
                Log.objects.create(content_type='Mentor viewed all query', user_id=request.data['user_id'])
                response['status'] = 'success'
                response['queries'] = query
        else:
            response['messages'].append('User does not exists.')
        return Response(response)


class mentorRespondToQuery(APIView): 
    # permission_classes = (IsAuthenticated, )
    def post(self, request):
        response = {'status':'failed', 'messages':[]}
        respond_object = Query.objects.filter(id=request.data['query_id'], mentor_user_id=request.data['mentor_user_id']).values('response_message')
        if respond_object:
            respond = list(respond_object)
            if respond[0]['response_message']:
                response['messages'].append('You have already responded to this query.')
            else:
                instance = Query.objects.get(id=request.data['query_id'])
                form = QueryRespondForm(request.data or None, instance=instance)
                if form.is_valid():
                    form.save()
                    Log.objects.create(content_type='Mentor responded to query', user_id=request.data['mentor_user_id'])
                    response['status'] = 'success'
                    response['messages'].append('Your response has been sent.')
                else:
                    response['messages'].append('Response field cannot be left empty.')
        else:
            response['messages'].append('You can not respond to this query.')
        return Response(response)

@api_view(['GET', ])
def api_detail_query_view(request, slug):
    try:
        query_object = Query.objects.get(slug=slug)
    except query_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    if request.method == 'GET':
        serializer = QuerySerializer(query_object)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_query_view(request, slug):
    try:
        query_object = Query.objects.get(slug=slug)
    except query_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    if request.method == 'PUT':
        serializer = QuerySerializer(query_object, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE', ])
def api_delete_query_view(request, slug):
    try:
        query_object = Query.objects.get(slug=slug)
    except query_object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    if request.method == 'DELETE':
        operation = query_object.delete()
        data = {}
        if operation:
            data['success'] = 'deleted successful'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)


@api_view(['POST', ])
def api_create_query_view(request, slug):
    user_object = User.objects.get(pk=1)
    query_object = Query(author=user_object)    
    if request.method == 'POST':
        serializer = QuerySerializer(query_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

