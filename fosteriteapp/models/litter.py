from django.db import models
from .cat import Cat

class Litter(models.Model):
  
    '''
        Litter Model
        
        Arguments Required:
            name -- CharField
            mother -- Foreign Key for Cat
    '''
    
    name = models.CharField(max_length=55)
    mother = models.ForeignKey(
        Cat, 
        related_name="+",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name
