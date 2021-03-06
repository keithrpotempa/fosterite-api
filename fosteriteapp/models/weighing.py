from django.db import models
from .cat import Cat
from .foster import Foster

class Weighing(models.Model):
  
    '''
        Weighing Model
        
        Arguments Required:
            cat -- Foreign Key for Cat
            weight -- integer field
            user -- Foreign Key for Foster
            created_date -- datetime
            modified_date -- datetime
    '''
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    weight = models.IntegerField()
    user = models.ForeignKey(Foster, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.animal.name} weighed {self.weight}g on {self.created_date}"
