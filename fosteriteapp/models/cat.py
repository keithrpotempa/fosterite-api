from django.db import models
from django.db.models import F
from .foster import Foster
from .adoption_status import AdoptionStatus
from .litter import Litter

class Cat (models.Model):
    '''
        Cat Model:

        Arguments Required:
            creator -- foreign key for Foster
            birth_date -- date field
            name -- character field
            litter -- foreign key for Litter
            bonded_pair_cat -- foreign key for Cat (or null)
            sex -- character field
            fixed_date -- date field
            created_date -- datetime field
            modified_date -- datetime field
            adoption_status -- foreign key for AdoptionStatus
            image_path -- image field
            breed_id -- integer field 
              (foreign key for external stretch goal API Breed)
            adopted_date -- date field
            adopted_id -- foreign key for Foster 
    '''
    
    creator = models.ForeignKey(Foster, on_delete=models.DO_NOTHING)
    birth_date = models.DateField()
    name = models.CharField(max_length=50)
    litter = models.ForeignKey(Litter, on_delete=models.DO_NOTHING)
    bonded_pair_cat = models.ForeignKey(Cat, on_delete=models.DO_NOTHING)
    sex = models.CharField(max_length=10)
    fixed_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(auto_now=True)
    adoption_status = models.ForeignKey(AdoptionStatus, on_delete=models.DO_NOTHING)
    image_path = models.ImageField(blank=True, null=True)
    breed_id = models.IntegerField()
    adopted_date = models.DateField(blank=True, null=True)
    adopted_id = models.ForeignKey(Foster, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = (F('created_date').desc(nulls_last=True),)
