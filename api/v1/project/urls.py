from django.urls import path, include
from .views import ProjectViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProjectViewSets)

urlpatterns = [
    path('', include(router.urls)),
    # path("project/", ProjectViewSets.as_view()),
]