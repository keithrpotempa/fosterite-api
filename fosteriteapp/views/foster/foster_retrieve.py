from django.http import HttpResponseServerError
from rest_framework.response import Response
from fosteriteapp.models import Foster
from django.contrib.auth.models import User
from .foster_serializer import FosterSerializer
from .. import UserSerializer

def foster_retrieve(self, request, pk=None):
    """Handle GET requests for single foster

    Returns:
        Response -- JSON serialized foster instance
    """
    try:
        foster = User.objects.get(pk=pk)
        serializer = UserSerializer(foster, context={'request': request})
        return Response(serializer.data)
    except Exception as ex:
        return HttpResponseServerError(ex)
