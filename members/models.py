from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255,null=True)
    joined_date = models.DateField(null=True)
# Create your models here.

class Motorcycles(models.Model):
    tipe_of_motorcycle = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    value = models.FloatField(null=True)
    is_available = models.BooleanField()
    image=models.ImageField(upload_to="images/", blank=True,null=True)
    description = models.CharField(max_length=255)
    horsepower = models.FloatField(null=True)
    engine_capacity = models.IntegerField(null=True)

class Orders(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    oras = models.CharField(max_length=255)
    judet = models.CharField(max_length=255)
    adresa = models.CharField(max_length=255)
    denumire_produs = models.CharField(max_length=255,null=True)
    pret = models.FloatField(null=True)

class Facturare_pers_fizica(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    oras = models.CharField(max_length=255)
    judet = models.CharField(max_length=255)
    adresa = models.CharField(max_length=255)