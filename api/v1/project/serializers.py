# api.v1.project.serializers.py
# DRF
from rest_framework import serializers
# Django
from django.db import transaction
# Embedded
import re
# Internal
from api.v1.audio.utils import create_audio
from apps.project.models import Project
from .utils import preprocess

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectCreateSerializer(ProjectSerializer):
    text = serializers.ListField(
        child=serializers.CharField(),
        max_length=1,
        write_only=True
    )
    project = ProjectSerializer(read_only=True)

    @transaction.atomic()
    def create(self, validated_data):
        # 현재 유저 정보 가져오기
        current_user = self.context['request'].user

        # 새 프로젝트 아이디 값 구하기
        projects = Project.objects.filter(user=current_user).order_by('project_id')
        project_id = 1
        if len(projects) > 0:
            # 현재 유저의 마지막 프로젝트 아이디보다 1 큰 숫자로 설정
            project_id = projects[len(projects) - 1].project_id + 1

        # 프로젝트 생성하기
        project = Project.objects.create(
            project_title=validated_data['title'],
            user=current_user
        )
        project.project_id = project_id
        project.save()

        # 전처리 후 오디오 변환 함수에 넣기
        li = preprocess(validated_data['text'])
        res = create_audio(project, li)

        return project