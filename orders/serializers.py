from rest_framework import serializers
from .models import Order
import ipdb

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Order

        fields = [
            "id",
            "created_at",
            "updated_at",
            # "user",
            "address",
            "products",
            "order_products"
            # "delivery",
        ]
        depth = 1

    def create(self, validated_data: dict) -> Order:

        return Order.objects.create(**validated_data)
