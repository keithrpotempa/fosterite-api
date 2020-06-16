from django.http import HttpResponseServerError
from rest_framework.response import Response
from fosteriteapp.models import Foster
from django.contrib.auth.models import User
from .foster_serializer import FosterSerializer
from .. import UserSerializer

def foster_list(self, request):
    """Handle GET requests to fosters resource. 

    Returns:
        Response -- JSON serialized foster list
    """

    try:
        many = True
        user = User.objects.all()

        serializer = UserSerializer(
            user, many=many, context={'request': request})

        return Response(serializer.data)
    except Exception as ex:
        return HttpResponseServerError(ex)