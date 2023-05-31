
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ColorViewSet
router = DefaultRouter()
router.register('color', ColorViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
