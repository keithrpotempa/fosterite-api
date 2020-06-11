from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.utils import timezone
from .cat_serializer import CatSerializer
from fosteriteapp.models import Cat

class Cats(ViewSet):

    def list(self, request):
        """Handle GET requests for a list of cats
        
        Returns:
          Response -- JSON serialized list of cats
        """
        cats = Cat.objects.all()
        
        serializer = CatSerializer(
          cats, many=True, context={'request': request}
        )        
        
        return Response(serializer.data)
      
    def retrieve(self, request, pk=None):
        """Handle GET requests for single cat

        Returns:
            Response -- JSON serialized cat instance
        """
        try:
            cat = Cat.objects.get(pk=pk)

            serializer = CatSerializer(
                cat, many=False, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)