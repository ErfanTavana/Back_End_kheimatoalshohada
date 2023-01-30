from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views
urlpatterns = [
    path("Account/", views.Register, name="Account_name"),
    path("", views.home, name="Home_name"),
]