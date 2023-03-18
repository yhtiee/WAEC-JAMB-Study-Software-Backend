from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/token",
        "/api/token/refresh"
    ]
    return Response(routes)


class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            serializer.validated_data['password'] = make_password(password)
            serializer.validated_data['is_active'] = True
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserProfile(APIView):
    def post(self, request):
        user = request.user
        if user :
            user_details = User.objects.filter(username=user.username).values()
            user_id = user_details[0]["id"]
            career_choice = request.data["career_choice"]
            educational_level = request.data["educational_level"]
            path = UserProfile.objects.create(user_id = user_id, career_choice=career_choice, educational_level=educational_level)
            path.save()
            return Response(data={
                "status":status.HTTP_201_CREATED,
                "success": "profile successfully updated"
            })
        return Response(data={
            "status":status.HTTP_404_NOT_FOUND,
            "error": "user dosent exist"
        })

            

