from rest_framework import serializers
from .models import Motorcycle


class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'make', 'year', 'model', 'created_at')
        model = Motorcycle