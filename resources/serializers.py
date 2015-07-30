from rest_framework import serializers
from .models import Resource, Type


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
