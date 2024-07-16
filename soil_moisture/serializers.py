from rest_framework import serializers
from soil_moisture.models import SoilMoistureData

class SoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilMoistureData
        fields = ['id','latitude','longitude','soil_moisture']