from rest_framework.viewsets import ViewSet
from django.http import HttpResponseServerError
from rest_framework.response import Response
from .cat_serializer import CatSerializer
from fosteriteapp.models import Cat
from .cat_list import cat_list
from .cat_retrieve import cat_retrieve
from .cat_destroy import cat_destroy
from .cat_create import cat_create 

class Cats(ViewSet):
    '''
        Master view for cats endpoint
    '''
    def list(self, request):
        return cat_list(self, request)
      
    def retrieve(self, request, pk=None):
        return cat_retrieve(self, request, pk)
        
    def destroy(self, request, pk=None):
        return cat_destroy(self, request, pk)
    
    def create(self, request):
        return cat_create(self, request)