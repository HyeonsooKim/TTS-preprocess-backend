# api.v1.project.urls.py
# DRF
from rest_framework.routers import DefaultRouter
# Django
from django.urls import path, include
# Internal
from .views import ProjectViewSets

router = DefaultRouter()
router.register(r'', ProjectViewSets)

urlpatterns = [
    path('', include(router.urls)),
]