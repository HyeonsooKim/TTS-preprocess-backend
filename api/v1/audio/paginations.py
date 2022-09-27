# api.v1.audio.paginations.py
# DRF
from rest_framework.pagination import PageNumberPagination

class AudioPagination(PageNumberPagination):
    page_size = 10