from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["POST","GET"])
def account(request):
    if request.method == "POST":
        data = request.data
        return  Response({"message":f'{data.get("fullName")}-{data.get("userName")}-{data.get("phoneNumber")}-{data.get("password")}-{data.get("repeatPassword")}'})
    return Response({"no post deta" : 'no post deta' })

