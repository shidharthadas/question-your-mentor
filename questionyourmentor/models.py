from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user

class User(AbstractBaseUser, PermissionsMixin):
    USER = 'Us'
    MENTOR = 'Me'
    USER_ROLES = [
        (USER, 'User'),
        (MENTOR, 'Mentor'),
    ]
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=150, null=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=0)
    is_superuser = models.BooleanField(default=0)
    role = models.CharField(max_length=6, choices=USER_ROLES, default=USER)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


def attachment_path(instance, filename, **kwargs):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor_user_id = models.IntegerField(null=False, blank=False)
    query_message = models.TextField(null=False, blank=False, max_length=300)
    attachment = models.FileField(upload_to=attachment_path)
    query_time = models.DateTimeField(auto_now_add=True)
    response_message = models.TextField(blank=True)
    response_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.query_message


class Log(models.Model):
    action_time = models.DateTimeField(auto_now_add=True)
    content_type = models.TextField(null=False, blank=False, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.content_type
