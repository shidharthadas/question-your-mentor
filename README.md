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

# Setting up

Change the database credentials accordingly. In my case I am using MySql.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'database_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost_or_IP_Address',
        'PORT': '3306',
    }
}
```

Install using `pip`

    pip install -r requirements.txt

Startup up a new project like so...

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

Run the project using

    python manage.py runserver

Urls are

    - http://127.0.0.1:8000/swagger/

    - http://127.0.0.1:8000/api/register/

    - http://127.0.0.1:8000/api/login/

    - http://127.0.0.1:8000/api/token/refresh/

    - http://127.0.0.1:8000/api/user-sending-query/

    - http://127.0.0.1:8000/api/view-query/<int:pk>/

    - http://127.0.0.1:8000/api/mentor-respond-to-query/<int:pk>/

