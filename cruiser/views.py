from django.shortcuts import render
from .serializers import CourseSerializer, Lesson_MaterialSerializer
from .models import Course,Lesson_Material
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class Lesson_MaterialViewSet(ModelViewSet):
    queryset = Lesson_Material.objects.all()
    serializer_class = Lesson_MaterialSerializer