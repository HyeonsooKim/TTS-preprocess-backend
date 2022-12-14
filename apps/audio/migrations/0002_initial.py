# Generated by Django 4.1 on 2022-09-27 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddConstraint(
            model_name='audio',
            constraint=models.UniqueConstraint(fields=('audio_id', 'project_id'), name='unique_audio_project'),
        ),
    ]
