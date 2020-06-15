from rest_framework.response import Response
from fosteriteapp.models import Cat
from rest_framework import serializers
from rest_framework import status
from .cat_serializer import CatSerializer

def cat_list(self, request):
    """Handle GET requests for a list of cats
    
    Returns:
      Response -- JSON serialized list of cats
    """
    cats = Cat.objects.all()
    
    serializer = CatSerializer(
      cats, many=True, context={'request': request}
    )        
    
    return Response(serializer.data)