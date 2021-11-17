from rest_framework import serializers

from .models import Att


class AttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Att
        fields = '__all__'
