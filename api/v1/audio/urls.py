# api.v1.audio.urls.py
# DRF
from rest_framework.routers import DefaultRouter
# Django
from django.urls import path, include
# Internal
from .views import ProjectAudioListCreateView, ProjectAudioDetailView

urlpatterns = [
    path('', ProjectAudioListCreateView.as_view()),
    path('<int:pk>', ProjectAudioDetailView.as_view()),
]