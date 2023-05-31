from rest_framework import serializers
from home34.models import Color

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = "__all__"