from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path
from .views import UsersDetail, UsersSoftDelete, UsersList, register_view, UsersRestore

urlpatterns = [
    path("<int:pk>/", UsersDetail.as_view(), name="user-detailed"),
    path("", UsersList.as_view(), name="user-list"),
    path("register", register_view, name="register"),
    path("login", obtain_auth_token, name="login"),
    path("delete-user/<int:pk>/", UsersSoftDelete.as_view(), name="delete-user"),
    path("restore-deleted-user/<int:pk>/", UsersRestore.as_view(), name="restore-user"),
]
