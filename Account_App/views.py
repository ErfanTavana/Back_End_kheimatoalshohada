from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
import requests
from rest_framework.authentication import TokenAuthentication
# Create your views here.

@api_view(["POST","GET"])
def Register(request):
    if request.method == "POST":
        data = request.data
        user = User.objects.create_user(username=data.get("userName"),password=data.get("password"))
        add_token = Token.objects.get_or_create(user_id=user.id)
        user_token = Token.objects.get(user_id=user.id)
        return  Response({"access_token":f"{user_token}"},status=status.HTTP_201_CREATED)

