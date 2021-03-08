# Question Your Mentor

This project is based on Django REST framework. Below are the Use Case:

- Implement multiple API endpoints to post questions to Mentor.

- Application must be having user’s with two roles: User and Mentor. (Mentor will be created by the System Admin.)

- User should be able to register account and login.

- User must be able to send queries to Mentor. Message includes document attachment also.

- Mentor must be able to view and respond to all the queries received to him.

- Use customized user model and make email as username

- Use Django password validator. (Password should contain minimum 8 letters, 2 numbers and 2 special chars)

- Use JWT Authentication to protect the endpoints.

- Use DRF Exception Hander and return generic error response.

- Use Serializers to validate the user request

- Use multiple roles (e.g. USER, MENTOR,..) and the endpoints can be accessed based on the roles.

- Use SMTP email background(Gmail) and signals for notification (Optional)

- Log every endpoint access (Optional)

- Use Swagger for API documentation (Optional)

----

# Installation

Install using `pip`...

    pip install djangorestframework

Startup up a new project like so...

    pip install django
    pip install djangorestframework
    django-admin startproject example .
    ./manage.py migrate
    ./manage.py createsuperuser

Add the following to your `settings.py` module:

```python
INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```

Import the question-your-mentor.sql in your database and change the credentials accordingly.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'your_database_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost_or_IP_Address',
        'PORT': '3306',
    }
}
```