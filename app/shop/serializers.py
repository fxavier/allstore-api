from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category objects"""

    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for item objects"""

    class Meta:
        model = Item
        fields = ('title', 'price', 'discount_price', 'category', 'label', 'slug', 'description')
