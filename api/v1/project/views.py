# api.v1.project.views.py

# DRF
from rest_framework.generics import CreateAPIView, DestroyAPIView
# Django
from django.shortcuts import render
# Internal
from .serializers import ProjectCreateSerializer, ProjectSerializer
from apps.project.models import Project

# Create your views here.
class ProjectCreateView(CreateAPIView):
    """
    프로젝트를 생성합니다.
    - input
        text: 텍스트가 담긴 리스트(length = 1)
        title: 프로젝트 제목
    - output
        project: 생성된 프로젝트 정보
    """

    serializer_class = ProjectCreateSerializer


class ProjectDestroyView(DestroyAPIView):
    """ 해당 프로젝트를 삭제합니다. """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer