from django.contrib import admin
from .models import Etudiant,Cours,Salle,Enseignant
# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Salle)
admin.site.register(Cours)
admin.site.register(Enseignant)

