from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"query", views.QueryViewSet)

app_name = "qym_api"
urlpatterns = [
    path("", include(router.urls)),

    path('user-login/', views.userLogin.as_view(), name ='user_login'),
    path('user-sending-query/', views.userSendingQuery.as_view(), name ='user_sending_query'),
    path('view-query/', views.viewQuery.as_view(), name ='view_query'),
    path('mentor-respond-to-query/', views.mentorRespondToQuery.as_view(), name ='mentor_respond_to_query'),
]
