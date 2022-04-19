from django.contrib import admin
from .models import Professeur
# Register your models here.
@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom','email', 'chef_departement')