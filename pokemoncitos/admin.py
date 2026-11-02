from django.contrib import admin
from .models import Entrenador, Gimnasio, Pokemon

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('documento', 'nombre', 'apellido', 'medallas')
    search_fields = ('nombre', 'apellido', 'documento')

@admin.register(Gimnasio)
class GimnasioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'elemento', 'lider', 'insignia')
    search_fields = ('nombre', 'elemento')

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'elemento', 'naturaleza', 'entrenador', 'color_carta', 'accesorio')
    list_filter = ('elemento', 'color_carta')
    search_fields = ('nombre',)

# Register your models here.
