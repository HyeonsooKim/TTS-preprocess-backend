# api.v1.urls.py

# Django
from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('project/', include('api.v1.project.urls')),
    path('audio/', include('api.v1.audio.urls')),
]