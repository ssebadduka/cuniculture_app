from django.db import models
from django.urls import reverse

# from cuniculture_app.models.livestocks import Livestock

class Farm(models.Model):
    farm_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    in_charge = models.CharField(max_length=50)
    in_charge_contact = models.CharField(max_length=20)

    def __str__(self):
       return self.farm_name
    