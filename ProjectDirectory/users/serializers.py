from .models import CustomUser, Team
from rest_framework import serializers
from climbers.serializers import ClimberSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class TeamSerializer(serializers.ModelSerializer):
    speed_climber=ClimberSerializer()
    lead_climber=ClimberSerializer()
    boulder_climber=ClimberSerializer()
    class Meta:
        model = Team
        fields = ['date_created', 'speed_climber', 'lead_climber', 'boulder_climber']
        extra_kwargs = {'date_created': {'read_only': True}}

class UserDetailSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'teams']

class TeamSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['speed_climber', 'lead_climber', 'boulder_climber']