from django.urls import path
from .views import *

urlpatterns = [
    path("", UserListApi.as_view(), name="user_list"),
    path("<int:pk>/", UserDetailApi.as_view(), name="user_detail"),
    path("<int:pk>/update/", UserUpdateApi.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDeleteApi.as_view(), name="user_delete"),
    path("register/", UserRegisterApi.as_view(), name="user_create"),
    path("me/", UserMeApi.as_view(), name="user_me"),
]