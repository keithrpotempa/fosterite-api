from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from .foster_list import foster_list
from .foster_retrieve import foster_retrieve

class Fosters(ViewSet):
    def list(self, request):
        return foster_list(self, request)
      
    def retrieve(self, request, pk=None):
        return foster_retrieve(self, request, pk)