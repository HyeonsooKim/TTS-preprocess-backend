from django.db import models

class TimeStampedModel(models.Model):
    """
    created_at, updated_at 필드 생성을 위한 기본 모델
    """
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(TimeStampedModel):
    index = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(unique=True, null=False)
    project_title = models.CharField(max_length=100)
