from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
import requests
from rest_framework.authentication import TokenAuthentication
# Create your views here.
import datetime as dt
import random
from  .models import CodeLogin
@api_view(["POST"])
def Register(request):
    if request.method == "POST":
        data = request.data
        try:#If the username already exists, except is executed
            User.objects.get(username=data.get("phoneNumber"))
            return Response({"ٍEroor":"This phone number is registered"},status=status.HTTP_200_OK)
        except:#If the username already exists, except is executed
            min = dt.datetime.now().time()
            get_code = CodeLogin.objects.get(username=data.get("phoneNumber"))
            if get_code.verification_code == data.get("validCode")  and min <= get_code.expiration_date:
                user = User.objects.create_user(username=data.get("phoneNumber"),first_name=data.get("firstName"),last_name=data.get("lastName"),password=data.get("password"))
                add_token = Token.objects.get_or_create(user_id=user.id)
                user_token = Token.objects.get(user_id=user.id)
                return Response(
                    {"access_token": f"{user_token}", 'phoneNumber': user.username, 'firstName':' "user"."first_name"',
                     'lastName': "user.last_name"}, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(["POST"])
def verification_code(request):
    if request.method == "POST":
        data = request.data
        try:
            code_all_get = CodeLogin.objects.get(username=data.get("phoneNumber"))
            code_all_get.delete()
        except:
            pass
        random_code = random.randint(10000, 99999)  # ایجاد تصادفی یک عدد پنج رقمی
        time_end = (dt.datetime.today() + dt.timedelta(minutes=2)).time()
        CodeLogin.objects.create(username=data.get("phoneNumber") , verification_code=random_code,expiration_date=time_end)
        return Response({"code ersal" :"oK"} ,status=status.HTTP_202_ACCEPTED)
@api_view(["POST"])
def Login(request):
    if request.method == "POST":
        data = request.data
        try:
            user =User.objects.get(username=data.get("phoneNumber"),password=data.get("password"))
            user_token = Token.objects.get(user_id=user.id)
            return  Response({"access_token":f"{user_token}",'phoneNumber':user.username,'firstName':user.first_name,'lastName':user.last_name},status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


