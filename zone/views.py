from rest_framework import viewsets
from .serializers import StateCreateSerializer,StateListSerializer
from .models import State


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()

    def get_serializer_class(self):
        if self.action=='list':
            return StateListSerializer
        else:
            return StateCreateSerializer

