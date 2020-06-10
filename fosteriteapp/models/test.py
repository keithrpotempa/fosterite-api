from django.db import models
from .animal import Animal

class Test(models.Model):
  
    '''
        Test Model
        
        Arguments Required:
            name -- CharField
            animal -- Foreign Key for Animal
            date -- datefield
            tested_positive -- boolean
    '''
    
    name = models.CharField(max_length=55)
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    date = models.DateField()
    tested_positive = models.BooleanField()


    def __str__(self):
        return self.name
