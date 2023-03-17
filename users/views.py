from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/login",
        "/api/token/refresh"
    ]
    return Response(routes)


class SignUp(APIView):
    def post(self, request):
        if request.method == "POST":
            last_name = request.POST["last_name"]
            first_name = request.POST["first_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]

            check_mail = User.objects.filter(email=email)
            check_user = User.objects.filter(username=username)

            if len(check_mail) > 0:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    "error":"user with mail already exist"
                })
            elif len(check_user) > 0:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    "error":"user with username already exist"
                })
            
            user = User.objects.create(username=username, last_name = last_name, first_name=first_name, email=email, password=password,)
            user.save()

            return Response(status=status.HTTP_201_CREATED, data={
                    "success":"user created"
                })
        return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    "error":"only POST request allowed on this view"
                })


# class CreateCourseCombinationJamb(APIView):
#     def post(self, request):
#         user = request.user
#         if user :
#             user_details = User.objects.filter(username=user).values()
#             user_id = user_details[0]["id"]
#             course = user_details[0]["career_choice"]
            

