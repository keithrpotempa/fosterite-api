from rest_framework.response import Response
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from .cat_serializer import CatSerializer
from fosteriteapp.models import Cat

def cat_retrieve(self, request, pk=None):
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