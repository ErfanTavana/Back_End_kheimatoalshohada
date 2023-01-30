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
        try:#If the username already exists, except is executed
            User.objects.get(username=data.get("phoneNumber"))
            return Response(status=status.HTTP_200_OK)
        except:#If the username already exists, except is executed
            user = User.objects.create_user(username=data.get("phoneNumber"),first_name=data.get("firstName"),last_name=data.get("lastName"),password=data.get("password"))
            add_token = Token.objects.get_or_create(user_id=user.id)
            user_token = Token.objects.get(user_id=user.id)
            return  Response({"access_token":f"{user_token}"},status=status.HTTP_201_CREATED)