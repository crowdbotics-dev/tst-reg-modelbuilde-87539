from rest_framework import authentication
from home1.models import Home10
from .serializers import Home10Serializer
from rest_framework import viewsets

class Home10ViewSet(viewsets.ModelViewSet):
    serializer_class = Home10Serializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Home10.objects.all()