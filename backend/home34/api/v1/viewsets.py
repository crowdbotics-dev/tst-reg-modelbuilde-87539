from rest_framework import authentication
from home34.models import Color
from .serializers import ColorSerializer
from rest_framework import viewsets

class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Color.objects.all()