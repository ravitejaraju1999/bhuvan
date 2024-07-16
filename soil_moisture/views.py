from django.shortcuts import render
from soil_moisture.models import SoilMoistureData
from soil_moisture.serializers import SoilSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class SoilMoistViewSet(viewsets.ModelViewSet):

    queryset = SoilMoistureData.objects.all()
    serializer_class = SoilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','latitude','longitude']# it will just fletch accurate match
    #filter_backends = [filters.SearchFilter]
    search_fields = ['=id','=latitude','=longitude'] # "^" it is uses to search who are starts with, "=" it fletches which are exactly matches ,  '$' based on regular expressions




