import json
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from fosteriteapp.models import Foster


@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    try:
        new_user = User.objects.create_user(
            username=req_body['username'],
            email=req_body['email'],
            password=req_body['password'],
            first_name=req_body['first_name'],
            last_name=req_body['last_name']
        )

        foster = Foster.objects.create(
            user=new_user,
            looking_to_foster=req_body['looking_to_foster'],
            phone=req_body['phone_number'],
            street=req_body['street'],
            city=req_body['city'],
            state=req_body['state'],
            zip=req_body['zip'],
            created_date=timezone.now(),
            modified_date=timezone.now()
        )

        # Commit the user to the database by saving it
        foster.save()

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=new_user)

        # Return the token to the client
        data = json.dumps({"token": token.key})
        return HttpResponse(data, content_type='application/json')
        
    except Exception as x:
        return HttpResponse(x, content_type='application/json')
