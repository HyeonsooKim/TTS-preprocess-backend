from django.db import models
from apps.user.models import User
from django.conf import settings

class TimeStampedModel(models.Model):
    """
    created_at, updated_at 필드 생성을 위한 기본 모델
    """
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.IntegerField(unique=True, null=False)
    project_title = models.CharField(verbose_name='프로젝트 이름', max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project_id', 'user'], name='unique_project_user')
        ]