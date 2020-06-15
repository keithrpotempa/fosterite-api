from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.utils import timezone

from .adoption_status_serializer import AdoptionStatusSerializer
# Had to "import as" due to 
# the names being the same between
# view and model
from fosteriteapp.models import AdoptionStatus as AdoptionStatusModel

class AdoptionStatus(ViewSet):
  
    def list(self, request):
        """
          Handle GET requests to AdoptionStatus resource
          
          Returns:
            Response -- JSON serialized list of AdoptionStatus
        """
        
        status = AdoptionStatusModel.objects.all()
        
        serializer = AdoptionStatusSerializer(
            status, many=True, context={'request': request}
        )
        
        return Response(serializer.data)