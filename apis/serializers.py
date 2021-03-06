from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import (
    Advisory,
    Awareness,
    GovtData,
    Precaution,
    CoronaAudio,
    Requirement,
    Neighbour,
    DailyBasis,
    Home,
    Bank,
)

User = get_user_model()


class AdvisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisory
        fields = '__all__'


class AwarenessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awareness
        fields = '__all__'


class GovtDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovtData
        fields = '__all__'


class PrecautionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precaution
        fields = '__all__'


class CoronaAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoronaAudio
        fields = '__all__'


class NeighbourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbour
        fields = '__all__'


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'


class DailyBasisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyBasis
        fields = '__all__'


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
