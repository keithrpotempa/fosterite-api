from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.utils import timezone
from .cat_serializer import CatSerializer
from fosteriteapp.models import Cat

class Cats(ViewSet):

    def list(self, request):
        """Handle GET requests for a list of cats
        
        Returns:
          Response -- JSON serialized list of cats
        """
        cats = Cat.objects.all()
        
        serializer = CatSerializer(
          cats, many=True, context={'request': request}
        )        
        
        return Response(serializer.data)
      
    def retrieve(self, request, pk=None):
        """Handle GET requests for single cat

        Returns:
            Response -- JSON serialized cat instance
        """
        try:
            cat = Cat.objects.get(pk=pk)

            serializer = CatSerializer(
                cat, many=False, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def destroy(self, request, pk=None):
        """
        Handles DELETE requests for single cat
        """
        
        try:
            cat = Cat.objects.get(pk=pk)
            cat.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Cat.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        """
        Handle POST operations and returns JSON serialized cat instance
        
        Required Arguments:
            name, creator_id, sex, breed
        
        Optional Arguments:
            birth_date, litter_id, bonded_pair_cat_id, 
            fixed_date, image file, adoption_status_id,
            adopted_date, adopted_id
        """
        
        def optionalArg(arg):
            if arg in request.data:
                cat.arg = request.data[arg]
            else:
                cat.arg = None
        
        ## BASIC PROFILE
        cat = Cat()
        cat.name = request.data["name"]
        # TODO: instance instead of fk?
        cat.creator_id = request.data["creator_id"]
        cat.birth_date = request.data["birth_date"]
        # FIXME: implement if stretch goal reached
        cat.breed = 1
        cat.sex = request.data["sex"]
        
        ## Optional Arguments
        optionalArg("bonded_pair_cat_id")
        optionalArg("litter_id")
        optionalArg("fixed_date")
        # TODO: instance instead of fk?
        optionalArg("adoption_status_id")
        optionalArg("adopted_date")
        # TODO: instance instead of fk?
        optionalArg("adopted_id")
            
        ## IMAGE
        # If a user is uploading a file, 
        # assign it, otherwise skip this and allow it to be null
        if request.FILES:
        # "When Django handles a file upload, the file data ends up placed in request.FILES"
        # https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
            newproduct.image_path = request.FILES["image_path"]
        
        
        ## META DATA
        # https://stackoverflow.com/a/37607525/798303
        # Changed to timezone (from datetime) to fix a naive time error
        cat.created_date = timezone.now()
        cat.modified_date = timezone.now()
        
        cat.save()

        serializer = CatSerializer(
            cat, context={'request': request})

        return Response(serializer.data)