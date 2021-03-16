from django.conf import settings 
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.core.mail import send_mail, EmailMessage
from questionyourmentor.models import User, Query, Log
from .serializers import UserSerializer, QueryCreateSerializer, QueryRespondSerializer


def SendEmail(recipient_list, first_name):
    subject = 'Welcome to Question Your Mentor'
    message = f'Hi {first_name}, thank you for registering in Question Your Mentor.'
    email_from = settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from, recipient_list )


def SendEmailWithHtmlContent(recipient_list, first_name):
    subject = 'Welcome to Question Your Mentor'
    html_content = f'<h2>Welcome {first_name}</h2><h4>Thank you for registering in Question Your Mentor.</h4>'
    email_from = settings.EMAIL_HOST_USER
    email = EmailMessage(subject, html_content, email_from, recipient_list)
    email.content_subtype = "html"
    email.send()


def SendEmailWithAttachment(recipient_list, first_name):
    subject = 'Welcome to Question Your Mentor'
    html_content = f'<h2>Welcome {first_name}</h2><h4>Thank you for registering in Question Your Mentor.</h4>'
    email_from = settings.EMAIL_HOST_USER
    email = EmailMessage(subject, html_content, email_from, recipient_list)
    email.content_subtype = "html"
    fd = open('attach.py', 'r')
    email.attach('attach.py', fd.read(), 'text/plain')
    email.send()


class UserRegister(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            SendEmail([request.data["email"], ], request.data["first_name"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSendingQuery(APIView): 
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        user_object = User.objects.filter(id=request.data['user']).values('role')
        mentor_object = User.objects.filter(id=request.data['mentor_user_id']).values('role')
        if user_object and mentor_object:
            user = list(user_object)
            mentor = list(mentor_object)
            if 'User' == user[0]['role'] and 'Mentor' == mentor[0]['role']:
                serializer = QueryCreateSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    Log.objects.create(content_type='User sent a query', user_id=request.data['user'])
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={"detail": "Only role with User can sent query to Mentor."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"detail": "User not found."}, status=status.HTTP_400_BAD_REQUEST)


class ViewQuery(APIView): 
    permission_classes = (IsAuthenticated, )
    def get(self, request, pk):
        user_object = User.objects.filter(id=pk).values('role')
        if user_object:
            user = list(user_object)
            if 'User' == user[0]['role']:
                query_object = Query.objects.filter(user_id=pk).values('id', 'query_message', 'attachment', 'mentor_user_id', 'response_message')
                query = list(query_object)
                Log.objects.create(content_type='Viewed all query', user_id=pk)
                return Response(query)
            elif 'Mentor' == user[0]['role']:
                query_object = Query.objects.filter(mentor_user_id=pk).values('id', 'user_id', 'query_message', 'attachment', 'response_message')
                query = list(query_object)
                Log.objects.create(content_type='Viewed all query', user_id=pk)
                return Response(query)
        else:
            return Response(data={"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class MentorRespondToQuery(APIView): 
    permission_classes = (IsAuthenticated, )
    def get_object(self, pk):
        try:
            return Query.objects.get(pk=pk)
        except Query.DoesNotExist:
            raise Http404
    
    def put(self, request, pk):
        query = self.get_object(pk)
        serializer = QueryRespondSerializer(query, data=request.data)
        if serializer.is_valid():
            respond_object = Query.objects.filter(id=pk, mentor_user_id=request.data['mentor_user_id']).values('response_message')
            if respond_object:
                respond = list(respond_object)
                if respond[0]['response_message']:
                    return Response(data={"detail": "You have already responded to this query."}, status=status.HTTP_400_BAD_REQUEST)
                else:                    
                    serializer.save()
                    Log.objects.create(content_type='Mentor responded to query', user_id=request.data['mentor_user_id'])
                    return Response(serializer.data)
            else:
                return Response(data={"detail": "You can not respond to this query."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
