
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Home10ViewSet
router = DefaultRouter()
router.register('home10', Home10ViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
