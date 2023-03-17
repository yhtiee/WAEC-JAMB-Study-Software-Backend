from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

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