from rest_framework import serializers
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