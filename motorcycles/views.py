from rest_framework import generics
from .models import Motorcycle
from .permissions import IsOwnerOrReadOnly
from .serializers import MotorcycleSerializer


class MotorcycleList(generics.ListCreateAPIView):
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer


class MotorcycleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer