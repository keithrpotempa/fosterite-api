from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from fosteriteapp.models import Cat

class CatSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Cats

    Arguments:
        serializers
    """

    class Meta:
        model = Cat
        url = serializers.HyperlinkedIdentityField(
            view_name='cats',
            lookup_field='id'
        )

        fields = ('id', 'creator_id', "birth_date", "name",
                "litter_id", "bonded_pair_cat_id", "sex",
                "fixed_date", "created_date", "modified_date",
                "adoption_status_id", "image_path", "breed",
                "adopted_date", "adopted_id", "adoption_status"
        )
        
        depth = 1