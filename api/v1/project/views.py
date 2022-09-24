from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializers
from apps.project.models import Project

# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers