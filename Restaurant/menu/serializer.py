from rest_framework import serializers

from menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'price']


class FullMenuSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    restaurant_id = serializers.IntegerField(source='restaurant.id', read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'restaurant_id', 'restaurant_name','name', 'description', 'price']


class MenuRestaurantSerializer(serializers.Serializer):
    restaurant = serializers.CharField()
    menu = MenuSerializer(many=True)
