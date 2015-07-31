from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Resource, Type
from .serializers import ResourceSerializer, TypeSerializer


class ResourceViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    """
    A simple ViewSet for listing or retrieving resourcess.

    CREATE: curl -XPOST http://192.168.100.3:8000/api/v1/resources/ --data "title=test1&url=test1&types=5171003185430528"  -H 'Authorization: Token 6f55ef5ccf15fa25f8d4e2ba1d75e316c04d7bb0'
    UPDATE: curl -XPUT http://192.168.100.3:8000/api/v1/resources/5079606281371648/ --data "name=python3&tag=python3"
    PATCH: curl -XPATCH http://192.168.100.3:8000/api/v1/resources/5079606281371648/ --data "name=python4"
    DELETE: curl -XDELETE http://192.168.100.3:8000/api/v1/resources/5079606281371648/
    """
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()

    @api_view(('GET',))
    @authentication_classes((TokenAuthentication,))
    @permission_classes((IsAuthenticated,))
    def list(self, request):
        queryset = Resource.objects.all()
        serializer = ResourceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Resource.objects.all()
        resource = get_object_or_404(queryset, pk=pk)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

    @permission_classes(IsAuthenticated)
    def create(self, request, *args, **kwargs):
        return super(ResourceViewSet, self).create(request, *args, **kwargs)


class TypeViewSet(viewsets.ModelViewSet):

    # authentication_classes = (TokenAuthentication,)

    """
    A simple ViewSet for listing or retrieving types:

    CREATE: curl -XPOST http://192.168.100.3:8000/api/v1/types/ --data "name=python2&tag=python2"
    UPDATE: curl -XPUT http://192.168.100.3:8000/api/v1/types/5079606281371648/ --data "name=python3&tag=python3"
    PATCH: curl -XPATCH http://192.168.100.3:8000/api/v1/types/5079606281371648/ --data "name=python4"
    DELETE: curl -XDELETE http://192.168.100.3:8000/api/v1/types/5079606281371648/
    """
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
