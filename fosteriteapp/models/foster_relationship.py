from django.db import models
from .animal import Animal
from .foster import Foster

class FosterRelationship(models.Model):
  
    '''
        Foster Relationship Model
        
        Arguments Required:
            animal -- Foreign Key for Animal
            foster -- Foreign Key for Foster
            start_date -- date field
            end_date -- date field, can be null            
    '''
    
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    foster = models.ForeignKey(Foster, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.animal.name} fostered by {self.foster.user.first_name} {self.foster.user.last_name}"
