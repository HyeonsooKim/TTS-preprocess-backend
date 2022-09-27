# api.v1.project.views.py

# DRF
from rest_framework import viewsets
# Django
from django.shortcuts import render
# Internal
from .serializers import ProjectSerializers
from apps.project.models import Project

# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers