
from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path("", views.inicio, name="inicio"),

    # Pokémon
    path("pokemon/crear/", views.crear_pokemon, name="crear_pokemon"),
    path("pokemon/editar/<int:id>/", views.editar_pokemon, name="editar_pokemon"),
    path("pokemon/eliminar/<int:id>/", views.eliminar_pokemon, name="eliminar_pokemon"),

    # Gimnasios
    path("gimnasio/crear/", views.crear_gimnasio, name="crear_gimnasio"),
    path("gimnasio/editar/<int:id>/", views.editar_gimnasio, name="editar_gimnasio"),
    path("gimnasio/eliminar/<int:id>/", views.eliminar_gimnasio, name="eliminar_gimnasio"),

    # Entrenadores
    path("entrenador/crear/", views.crear_entrenador, name="crear_entrenador"),
    path("entrenador/editar/<int:id>/", views.editar_entrenador, name="editar_entrenador"),
    path("entrenador/eliminar/<int:id>/", views.eliminar_entrenador, name="eliminar_entrenador"),

    # Pokedex
    path("pokedex/", views.pokedex, name="pokedex"),


]


