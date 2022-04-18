from django.db import models

# Create your models here.

class Professeur(models.Model):
    prenom = models.CharField(max_length=300)
    nom = models.CharField(max_length=300)
    email = models.EmailField(max_length=255,null=True)
    contact_prof = models.CharField(max_length=300)
    date_d_adhesion = models.DateField(blank=False, null=False)
    chef_departement = models.BooleanField(default=False, blank=True)