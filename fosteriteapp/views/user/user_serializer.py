from django.contrib.auth.models import User
from rest_framework import serializers
from fosteriteapp.models import Foster

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for users

    Arguments:
        serializers
    """
    
    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user',
            lookup_field='id'
        )

        fields = ('first_name', 'last_name', "last_login",
                  "username", "email", "date_joined",)