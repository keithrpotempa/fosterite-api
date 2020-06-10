from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.utils import timezone
from .cat_serializer import CatSerializer

class Cats(ViewSet):

    def list(self, request):

        serializer = CatSerializer(
          cats, many=True, context={'request': request}
        )        
        
        return Response(serializer.data)