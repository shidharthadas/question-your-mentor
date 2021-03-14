from rest_framework import serializers
from questionyourmentor.models import User, Query
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


class QueryCreateSerializer(serializers.ModelSerializer):
    attachment = serializers.FileField(required=False)
    class Meta:
        model = Query
        fields = ('user', 'mentor_user_id', 'query_message', 'attachment', )


class QueryRespondSerializer(serializers.ModelSerializer):
    mentor_user_id = serializers.ReadOnlyField()
    response_message = serializers.CharField(required=True, allow_blank=False, max_length=300)
    class Meta:
        model = Query
        fields = ('mentor_user_id', 'response_message', )