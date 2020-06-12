from django.db import models
from .cat import Cat
from .foster import Foster

class FosterRelationship(models.Model):
  
    '''
        Foster Relationship Model
        
        Arguments Required:
            cat -- Foreign Key for Cat
            foster -- Foreign Key for Foster
            start_date -- date field
            end_date -- date field, can be null            
    '''
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    foster = models.ForeignKey(Foster, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.animal.name} fostered by {self.foster.user.first_name} {self.foster.user.last_name}"
