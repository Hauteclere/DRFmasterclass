from .models import Climber
from rest_framework import serializers

class ClimberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climber
        fields = ['id', 'name', 'specialty']

    def create(self, validated_data):
        return Climber.objects.create(**validated_data)