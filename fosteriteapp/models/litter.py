from django.db import models
from .animal import Animal

class Litter(models.Model):
  
    '''
        Litter Model
        
        Arguments Required:
            name -- CharField
            mother -- Foreign Key for Animal
    '''
    
    name = models.CharField(max_length=55)
    mother = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
