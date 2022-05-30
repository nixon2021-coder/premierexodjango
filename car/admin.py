from django.contrib import admin
from .models import Voiture
from django.utils.safestring import  mark_safe

class VoitureAdmin(admin.ModelAdmin):
    list_display = ('marque', 'couleur', 'modele', 'annee', 'description' , 'images_view')
    search_fields = ['marque']


    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')





admin.site.register(Voiture, VoitureAdmin)

# Register your models here.
