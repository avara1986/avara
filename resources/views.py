from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Resource, Type
from .serializers import ResourceSerializer, TypeSerializer

class ResourceViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving resourcess.
    """
    def list(self, request):
        queryset = Resource.objects.all()
        serializer = ResourceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Resource.objects.all()
        resource = get_object_or_404(queryset, pk=pk)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

class TypeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving resourcess.
    """
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
