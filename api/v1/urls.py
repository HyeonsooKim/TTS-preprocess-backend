# api.v1.urls.py
# DRF
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# Django
from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('project/', include('api.v1.project.urls')),
    path('audio/', include('api.v1.audio.urls')),
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]