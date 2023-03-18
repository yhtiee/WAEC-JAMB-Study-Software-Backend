from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CoursesCombinationJAMBSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCombinationJamb
        fields = "__all__"

class CoursesCombinationWAECSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseCombinationWAEC
        fields = "__all__"

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
