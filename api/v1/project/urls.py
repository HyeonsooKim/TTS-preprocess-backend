# api.v1.project.urls.py
# DRF
from rest_framework.routers import DefaultRouter
# Django
from django.urls import path, include
# Internal
from .views import ProjectCreateView, ProjectDestroyView


urlpatterns = [
    path('', ProjectCreateView.as_view()),
    path('<int:pk>', ProjectDestroyView.as_view()),
    path('<int:pk>/audio', include('api.v1.audio.urls')),
]