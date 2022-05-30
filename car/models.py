from email.mime import image
from django.db import models

# Create your models here.
class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    couleur = models.CharField(max_length=42)
    modele = models.CharField(max_length=100)
    annee = models.IntegerField()
    description = models.TextField(null=True)
    image = models.FileField()

    def __str__(self):
        return self.marque
