from rest_framework import serializers
from home1.models import Home10

class Home10Serializer(serializers.ModelSerializer):

    class Meta:
        model = Home10
        fields = "__all__"