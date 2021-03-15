from django.urls import path, include
from qym_api import views
from rest_framework_simplejwt import views as jwt_views

app_name = "qym_api"
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name ='user_register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name ='user_login'), 
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('user-sending-query/', views.UserSendingQuery.as_view(), name ='user_sending_query'),
    path('view-query/<int:pk>/', views.ViewQuery.as_view(), name ='view_query'),
    path('mentor-respond-to-query/<int:pk>/', views.MentorRespondToQuery.as_view(), name ='mentor_respond_to_query'),
]
