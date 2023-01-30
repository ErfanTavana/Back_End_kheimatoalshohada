from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views
urlpatterns = [
    path("Register/", views.Register, name="Register_name"),
    path("Verifi/", views.verification_code, name="VerifiAccount_name"),
    path("Login/", views.Login, name="Login_name"),



]