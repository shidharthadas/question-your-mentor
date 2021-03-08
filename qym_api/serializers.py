from rest_framework import serializers
from questionyourmentor.models import User, Query, Log
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'email', 'first_name', 'last_name', 'role')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role='User'
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('user_id', 'mentor_user_id', 'query_message', 'response_message')


class LogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model = Log
        fields = ('user', 'content_type')


class QueryFormSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    mentor_user_id = serializers.IntegerField(required=True)
    query_message = serializers.CharField(required=True, allow_blank=False, max_length=300)
    class Meta:
        model = Query
        fields = ('user', 'mentor_user_id', 'query_message', 'attachment', 'response_message')


class QueryFormWithAttachmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Query` instance, given the validated data.
        """
        return Query.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Query` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class QueryRespondSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
