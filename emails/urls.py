from django.urls import path
from .views import ListUserView

urlpatterns = [
  path("users/", ListUserView.as_view(), name="users_all"),
  path("users/<firstname>", ListUserView.as_view(), name="users_by_firstname")
]