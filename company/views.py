from rest_framework import viewsets
from . import serializers
from .models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = Company.objects.all()
