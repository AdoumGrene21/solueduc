from io import BytesIO
from PIL import Image

from django.core.files import File

from django.db import models

# Create your mode

class Salle(models.Model):
    libelle = models.CharField('Nom salle', max_length=120)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.libelle


class Type(models.Model):
    libelle = models.CharField('Nom Cours', max_length=120)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.libelle
   

class Cours(models.Model):
    libelle = models.CharField('Nom Cours', max_length=120)
    description = models.CharField(max_length=200, blank=True)
    vid = models.FileField(upload_to="video/", null=True)
    type = models.ForeignKey(Type, blank=False, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.libelle

    
class Enseignant(models.Model):
    nom = models.CharField('nom', max_length=120)
    prenoms = models.CharField('prenom', max_length=20)
   
    sexe = models.CharField('sexe', max_length=120)
    specialite = models.CharField('specialite', max_length=120)
    cours = models.ManyToManyField(Cours, blank=False)

        
    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    nom = models.CharField('Nom', max_length=120)
    prenoms = models.CharField('Prenoms', max_length=200)
    
    sexe = models.CharField('Sexe', max_length=120)
    address= models.CharField(max_length=200, blank=True)
    nationalite = models.CharField(max_length=120)
    salle = models.ForeignKey(Salle, blank=False, null=False, on_delete=models.CASCADE)
    cours = models.ManyToManyField(Cours,null=True, blank=True)


    def __str__(self):
        return self.nom



   # description = models.TextField(blank=True)
    #teachers = models.ManyToManyField(Teacher, blank=False)
    #courses = models.ManyToManyField(Coures, blank=False)
        