# api.v1.audio.views.py
# DRF
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Django
from django.shortcuts import render, get_object_or_404
# Internal
from .serializers import AudioSerializer, AudioCreateSerializer, AudioUpdateSerializer
from .paginations import AudioPagination
from apps.audio.models import Audio
from apps.project.models import Project
# Create your views here.

class ProjectAudioListCreateView(ListCreateAPIView):
    """
    해당 프로젝트의 텍스트를 조회하거나 생성합니다.
    GET
    - parameter
        page: 페이지 번호
    - output
        results: 해당 프로젝트의 오디오 리스트
    POST
    - input
        text: 생성할 문장
        project_id: 문장을 생성할 위치 (선택)
    - output
        audio: 생성된 오디오 정보
    """

    pagination_class = AudioPagination
    serializer_class = AudioSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        project_id = Project.objects.get(id=id)
        return Audio.objects.filter(project_id=project_id).order_by('audio_id')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AudioSerializer
        elif self.request.method == 'POST':
            return AudioCreateSerializer


class ProjectAudioDetailView(RetrieveUpdateDestroyAPIView):
    def get_object(self):
        project_id = get_object_or_404(Project, id=self.kwargs['pk'])
        return get_object_or_404(Audio, project_id=project_id, audio_id=self.kwargs['audio_id'])

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AudioSerializer
        elif self.request.method == 'PUT' or self.request.method == 'PATCH':
            return AudioUpdateSerializer