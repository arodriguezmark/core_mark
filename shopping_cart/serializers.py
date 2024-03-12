from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shopping_cart.models import ShoppingCart, Item
from users.models import User


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        shopping_cart = ShoppingCart.objects.create(**validated_data)
        for item_data in items_data:
            item = Item.objects.create(**item_data)
            shopping_cart.items.add(item)
            shopping_cart.total += item.total_price
        return shopping_cart


class ShowShoppingCartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = '__all__'
