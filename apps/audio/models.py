from django.db import models
from apps.common.models import TimeStampedModel
from apps.project.models import Project

# Create your models here.
class Audio(TimeStampedModel):
    SPEED = (
        (0.5, 0.5),
        (1.0, 1.0),
        (1.5, 1.5),
        (2.0, 2.0),
    )

    create_time = None
    text = models.TextField(verbose_name="변환 전 텍스트", default="")
    speed = models.FloatField(verbose_name="오디오 속도", choices=SPEED, default=1.0)
    audio_id = models.PositiveIntegerField(verbose_name="오디오 식별자", default=0, null=False)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['audio_id', 'project_id'], name='unique_audio_project')
        ]