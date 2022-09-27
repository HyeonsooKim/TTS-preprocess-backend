# api.v1.project.serializers.py
# DRF
from rest_framework import serializers
# Django
from django.db import transaction
# Embedded
import re
# Internal
from apps.project.models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectCreateSerializers(ProjectSerializers):
    text = serializers.ListField(
        child=serializers.CharField(),
        max_length=1,
        write_only=True
    )
    project = ProjectSerializers(read_only=True)

