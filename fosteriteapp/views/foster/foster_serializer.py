from django.http import HttpResponseServerError
from rest_framework import serializers
from fosteriteapp.models import Foster
from django.contrib.auth.models import User

class FosterSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for foster

    Arguments:
        serializers
    """

    class Meta:
        model = Foster
        url = serializers.HyperlinkedIdentityField(
            view_name='foster',
            lookup_field='id'
        )
        
        fields = ('id', 'looking_to_foster', 'phone', 'street',
                    'city', 'state', 'zip', 'created_date', 
                    'modified_date')

        # TODO: figure out how to utilize this
        # Excluding fields to display:
        # https://www.django-rest-framework.org/api-guide/serializers/#specifying-which-fields-to-include
        # exclude = ('url', 'user')

