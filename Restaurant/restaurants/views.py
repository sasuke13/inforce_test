from rest_framework import generics, permissions, mixins
from rest_framework.permissions import IsAuthenticated
from restaurants.models import Restaurants
from restaurants.permissions import IsAdmin
from restaurants.serializers import ReadCreateSerializer


class RestaurantAPIListView(generics.ListCreateAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = ReadCreateSerializer
    permission_classes = (IsAdmin,)


class RestaurantAPIUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = ReadCreateSerializer
    permission_classes = (IsAdmin, )
