from rest_framework import viewsets
from .serializers import StateSerializer
from .models import State


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
