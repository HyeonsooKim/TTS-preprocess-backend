# api.v1.audio.serializers.py
# DRF
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
# Django
from django.db import transaction
from django.shortcuts import get_object_or_404
# Internal
from apps.audio.models import Audio
from apps.project.models import Project
from api.v1.project.utils import preprocess

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'

class AudioCreateSerializer(AudioSerializer):
    def validate(self, attrs):
        # 현재 프로젝트의 오디오 목록 불러오기
        print('dir(self.context)', dir(self.context['view']), self.context['view'])
        current_user = self.context['request'].user
        pk = self.context.get('view').kwargs['pk']
        project_id = get_object_or_404(Project, user=current_user, id=pk)
        attrs['project_id'] = project_id
        audios = Audio.objects.filter(project_id=project_id).order_by('audio_id')

        # 아이디가 없거나 유효 범위를 벗어날 경우 마지막 아이디로 설정
        id = attrs.get('audio_id', None)
        if not id or id <= 0 or id > len(audios) + 1:
            attrs['audio_id'] = len(audios) + 1

        # 텍스트 전처리
        attrs['text'] = preprocess(attrs['text'])
        if len(attrs['text']) == 0:
            raise ValidationError({'text', '빈 문장입니다.'})

        return attrs

    @transaction.atomic()
    def create(self, validated_data):
        # 뒤에 있는 아이디 1씩 증가
        audios = Audio.objects.filter(
            project_id=validated_data['project_id'],
            audio_id__gte=validated_data['audio_id']
        ).order_by('-audio_id')
        for audio in audios:
            audio.audio_id += 1
            audio.save()

        # 오디오 생성
        return Audio.objects.create(**validated_data)

class AudioUpdateSerializer(AudioSerializer):
    audio_id = serializers.IntegerField(read_only=True)