from rest_framework import viewsets, mixins

from core.models import Category, Item

from . import serializers


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage categories in the database"""
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ItemViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage items in the database"""
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer
