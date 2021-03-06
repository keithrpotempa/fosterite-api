from django.db import models
from .cat import Cat

class Vaccination(models.Model):
  
    '''
        Vaccination Model
        
        Arguments Required:
            cat -- Foreign Key for Cat
            fvrcp1 -- boolean
            fvrcp2 -- boolean
            rabies -- boolean
            date -- datefield
    '''
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    fvrcp1 = models.BooleanField()
    fvrcp2 = models.BooleanField()
    rabies = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        return self.name
