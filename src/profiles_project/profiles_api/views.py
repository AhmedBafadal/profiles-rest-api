from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from . import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, etc)',
            'similar to traditional django view',
            'gives you control over your logic',
            'is mapped manually to URLs'
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with name"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """Handles updating an object."""
        return Response({'method':'put'})
    
    def patch(self, request, pk=None):
        """Handles updating fields provided in request for an object."""
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Handles deleting an object."""
        return Response({'method':'delete'})