from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .foster import Foster
from .adoption_status import AdoptionStatus

class Cat(models.Model):
    
    '''
        Cat Model:

        Arguments Required:
            creator -- foreign key for Foster
            birth_date -- date field
            name -- character field
            litter -- foreign key for Litter
            bonded_pair_cat -- foreign key for Animal (or null)
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
    
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    birth_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50)
    #https://stackoverflow.com/questions/44601550/how-to-solve-the-circular-import-error-in-django
    litter = models.ForeignKey(
        to="fosteriteapp.litter", 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#foreignkey
    bonded_pair_cat = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    sex = models.CharField(max_length=10)
    fixed_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(auto_now=True)
    adoption_status = models.ForeignKey(AdoptionStatus, default=1, on_delete=models.DO_NOTHING)
    image_path = models.ImageField(blank=True, null=True)
    breed = models.IntegerField(default=1)
    adopted_date = models.DateField(blank=True, null=True)
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_name
    adopted = models.ForeignKey(
        User, 
        related_name="+",
        on_delete=models.SET_NULL,
        blank=True, 
        null=True
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = (F('created_date').desc(nulls_last=True),)
