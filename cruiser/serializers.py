from dataclasses import field
from .models import Course,Lesson_Material
from rest_framework import serializers
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class Lesson_MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson_Material
        fields = '__all__'