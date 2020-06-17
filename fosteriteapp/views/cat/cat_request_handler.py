import json
from fosteriteapp.models import Cat, Foster, AdoptionStatus
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def cat_request_handler(request, pk=None):
    """
    Handles the building of a cat instance for cat views create and update
    
    (contained in request)    
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
    
    # If a pk is provided, it is an edit,
    # so get the cat object to edit
    if pk:
      cat = Cat.objects.get(pk=pk)
      
    # Otherwise, it is a creation,
    # so start with a blank slate
    else:
      cat = Cat()
    
    ## BASIC PROFILE
    cat.name = request.data["name"]
    # Extracted from the user's token
    foster = Foster.objects.get(user=request.auth.user)
    cat.creator = foster
    cat.birth_date = request.data["birth_date"]
    # FIXME: implement if stretch goal reached
    cat.breed = 1
    cat.sex = request.data["sex"]
    cat.adoption_status = AdoptionStatus.objects.get(pk=request.data["adoption_status_id"])
    
    ## Optional Arguments
    optionalArg("bonded_pair_cat_id")
    optionalArg("litter_id")
    optionalArg("fixed_date")
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
    cat.modified_date = timezone.now()
    
    return cat