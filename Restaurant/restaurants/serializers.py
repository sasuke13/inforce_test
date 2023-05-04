from rest_framework import serializers

from restaurants.models import Restaurants


class ReadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = "__all__"

