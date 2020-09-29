from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class RegistrationData(models.Model):
    full_name = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=60)
    name_of_subject= models.CharField(max_length=60)


    def __str__(self):
        return '{}'.format(self.full_name)

