from django.utils import timezone
from django.http import HttpResponseServerError
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .cat_serializer import CatSerializer
from .cat_request_handler import cat_request_handler

@login_required
def cat_create(self, request):
    """
    Handle POST operations and returns JSON serialized cat instance
    
    Required Arguments:
        name, creator_id, sex, breed
    
    Optional Arguments:
        birth_date, litter_id, bonded_pair_cat_id, 
        fixed_date, image file, adoption_status_id,
        adopted_date, adopted_id
    """
    
    cat = cat_request_handler(request)
    # On a create, the created date must also be appended
    cat.created_date = timezone.now()
    cat.save()

    serializer = CatSerializer(
        cat, context={'request': request})

    return Response(serializer.data)