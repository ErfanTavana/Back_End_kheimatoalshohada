from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views
urlpatterns = [
    path("",views.account,name="Account_name"),
]