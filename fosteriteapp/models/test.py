from django.db import models
from .cat import Cat

class Test(models.Model):
  
    '''
        Test Model
        
        Arguments Required:
            name -- CharField
            animal -- Foreign Key for Cat
            date -- datefield
            tested_positive -- boolean
    '''
    
    name = models.CharField(max_length=55)
    cat = models.ForeignKey(Cat, on_delete=models.DO_NOTHING)
    date = models.DateField()
    tested_positive = models.BooleanField()


    def __str__(self):
        return self.name
