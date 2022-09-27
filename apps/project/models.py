# apps.project.models.py

# Django
from django.db import models
from django.conf import settings

# Internal
from apps.common.models import TimeStampedModel

class Project(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.IntegerField(unique=True, null=False)
    project_title = models.CharField(verbose_name='프로젝트 이름', max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project_id', 'user'], name='unique_project_user')
        ]