"""View module for handling requests about payments"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from fosteriteapp.models import AdoptionStatus

class AdoptionStatusSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Adoption Statuses

    Arguments:
        serializers
    """

    class Meta:
        model = AdoptionStatus
        url = serializers.HyperlinkedIdentityField(
            view_name='adoptionstatus',
            lookup_field='id'
        )

        fields = ('id', 'name')
