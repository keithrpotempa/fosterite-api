from django.db import models
from django.urls import reverse
from django.db.models import F
from django.contrib.auth.models import User


class Foster(models.Model):
    '''
        Foster Model 
        
        Arguments Required:
          user--user 1-1 field
          looking_to_foster boolean
          phone-character field
          street- character field
          city - character field
          state - character field
          zip - integer field
          created_date - datetime
          modified_date - datetime
    '''
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    looking_to_foster = models.models.BooleanField(null=True, blank=True, default=False)
    phone = models.CharField(max_length=20)    
    street = models.CharField(max_length=55)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()
    created_date = models.DateTimeField()
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.DateField.auto_now
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = (F('user__date_joined').asc(nulls_last=True),)