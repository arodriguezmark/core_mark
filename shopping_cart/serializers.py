from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shopping_cart.models import ShoppingCart, Item
from users.models import User


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
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
        return shopping_cart

    def validate(self, attrs):
        customer_id = attrs['customer_id']

        existing_cart = ShoppingCart.objects.filter(customer_id=customer_id).exists()
        if existing_cart:
            raise serializers.ValidationError({"customer_id": "customer already have a shopping cart"})
        return attrs