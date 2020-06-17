from rest_framework.response import Response
from fosteriteapp.models import Cat
from rest_framework import status
from .cat_request_handler import cat_request_handler

def cat_update(self, request, pk=None):
    """
      Handles PUT requests for cat endpoint view
      
      Required Arguments:
          name, creator_id, sex, breed
    
      Optional Arguments:
          birth_date, litter_id, bonded_pair_cat_id, 
          fixed_date, image file, adoption_status_id,
          adopted_date, adopted_id
    """

    cat = cat_request_handler(request, pk)
    cat.save()
    return Response({}, status=status.HTTP_204_NO_CONTENT)
