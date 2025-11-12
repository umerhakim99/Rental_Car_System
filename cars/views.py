from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'model', 'rent_per_month']
