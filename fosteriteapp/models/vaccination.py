from django.db import models
from .Animal import Animal

class Vaccination(models.Model):
  
    '''
        Vaccination Model
        
        Arguments Required:
            name -- CharField
            animal -- Foreign Key for Animal
            fvrcp1 -- boolean
            fvrcp2 -- boolean
            rabies -- boolean
            date -- datefield
    '''
    
    name = models.CharField(max_length=55)
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    fvrcp1 = models.BooleanField()
    fvrcp2 = models.BooleanField()
    rabies = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        return self.name
