from django.db import models
from django.urls import reverse

from .farms import Farm

class Livestock(models.Model):

    status_options = [
        ('Birth', 'Birth'),
        ('Stock', 'Stock')
    ]

    breed_options = [
        ('Breeder', 'Breeder'),
        ('Beef', 'Beef')
    ]

    maturity_options = [
        ('day', 'Day'),
        ('week', 'Week'),
    ]

    livestock_type = models.CharField(max_length=50)
    breed_category = models.CharField(max_length=50, choices=breed_options)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    male = models.IntegerField()
    female = models.IntegerField()
    maturity = models.IntegerField()
    maturity_period = models.CharField(max_length=15, choices=maturity_options)
    available_stock = models.IntegerField()
    status = models.CharField(max_length=50, choices=status_options)
    stock_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Livestock")
        verbose_name_plural = ("Livestocks")

    def __str__(self):
        return f"{self.id} - {self.livestock_type} ({self.breed_category})"

    def get_absolute_url(self):
        return reverse("Livestock_detail", kwargs={"pk": self.pk})

class Deaths(models.Model):

    gender_options = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    death_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    gender = models.CharField(max_length=50, choices=gender_options)
    cause = models.TextField()

    class Meta:
        verbose_name = ("Deaths")
        verbose_name_plural = ("Deathss")

    def __str__(self):
        return self.farm

    def get_absolute_url(self):
        return reverse("Deaths_detail", kwargs={"pk": self.pk})

class Sales(models.Model):

    sales_date = models.DateField(auto_now=True)
    client = models.CharField(max_length=50)
    total_quantity = models.IntegerField(blank=True, null=True, default=0)
    total_amount = models.DecimalField(max_digits=6, decimal_places=0,blank=True, null=True, default=0)

    class Meta:
        verbose_name = ("Sales")
        verbose_name_plural = ("Saless")

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse("Sales_detail", kwargs={"pk": self.pk})

class SalesDetails(models.Model):

    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    male = models.IntegerField()
    female = models.IntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = ("SalesDetails")
        verbose_name_plural = ("SalesDetailss")

    def __str__(self):
        return self.livestock

    def get_absolute_url(self):
        return reverse("SalesDetails_detail", kwargs={"pk": self.pk})

