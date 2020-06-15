from rest_framework.response import Response
from fosteriteapp.models import Cat
from rest_framework import serializers
from rest_framework import status
from .cat_serializer import CatSerializer

def cat_destroy(self, request, pk=None):
    """
    Handles DELETE requests for single cat
    """
    
    try:
        cat = Cat.objects.get(pk=pk)
        cat.delete()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    except Cat.DoesNotExist as ex:
        return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
