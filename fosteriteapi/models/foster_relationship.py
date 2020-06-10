from django.db import models
from . import Cat, Foster

class FosterRelationship (models.Model):
  
    '''
        Foster Relationship Model
        
        Arguments Required:
            cat -- Foreign Key for Cat
            foster -- Foreign Key for Foster
            start_date -- date field
            end_date -- date field, can be null            
    '''
    
    cat = models.ForeignKey(Cat, on_delete=models.DO_NOTHING)
    foster = models.ForeignKey(Foster, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{cat.name} fostered by {foster.user.first_name} {foster.user.last_name}"
