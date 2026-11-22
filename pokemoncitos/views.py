
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pokemon, Gimnasio, Entrenador
from .forms import PokemonForm,GimnasioForm,EntrenadorForm
from .decoradores import rol_requerido




def inicio(request):
    import requests

    pokemones = Pokemon.objects.all()
    gimnasios = Gimnasio.objects.all()
    entrenadores = Entrenador.objects.all()

    # Traducción de los tipos al español
    traducciones_tipos = {
        "fire": "Fuego",
        "water": "Agua",
        "grass": "Planta",
        "electric": "Eléctrico",
        "psychic": "Psíquico",
        "normal": "Normal",
        "ice": "Hielo",
        "fighting": "Lucha",
        "poison": "Veneno",
        "ground": "Tierra",
        "flying": "Volador",
        "bug": "Bicho",
        "rock": "Roca",
        "ghost": "Fantasma",
        "dragon": "Dragón",
        "steel": "Acero",
        "dark": "Siniestro",
        "fairy": "Hada"
    }

    for pokemon in pokemones:
        pokemon.estadisticas_api = {}
        pokemon.imagen_api = None
        pokemon.tipos_api = []

        try:
            nombre_api = pokemon.nombre.strip().lower()

            respuesta = requests.get(
                f"https://pokeapi.co/api/v2/pokemon/{nombre_api}",
                timeout=5
            )

            if respuesta.status_code == 200:
                datos = respuesta.json()

                # Imagen oficial del Pokémon
                pokemon.imagen_api = (
                    datos["sprites"]["other"]["official-artwork"]["front_default"]
                    or datos["sprites"]["front_default"]
                )

                # Tipos traducidos al español
                pokemon.tipos_api = [
                    traducciones_tipos.get(
                        tipo["type"]["name"],
                        tipo["type"]["name"].capitalize()
                    )
                    for tipo in datos["types"]
                ]

                # Estadísticas de combate
                for estadistica in datos["stats"]:
                    nombre = estadistica["stat"]["name"]
                    valor = estadistica["base_stat"]

                    pokemon.estadisticas_api[nombre] = valor

        except requests.RequestException:
            pass

    contexto = {
        "pokemones": pokemones,
        "gimnasios": gimnasios,
        "entrenadores": entrenadores,
    }

    return render(
        request,
        "pokemoncitos/inicio.html",
        contexto
    )






# REGISTRAR UN POKEMON

@rol_requerido("ADMIN", "EDITOR")
def crear_pokemon(request):
    if request.method == "POST":
        formulario = PokemonForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = PokemonForm()

    return render(
        request,
        "pokemoncitos/formulario_pokemon.html",
        {"formulario": formulario}
    )


# EDITAR UN POKEMON
@rol_requerido("ADMIN", "EDITOR")
def editar_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)

    if request.method == "POST":
        formulario = PokemonForm(request.POST, instance=pokemon)

        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = PokemonForm(instance=pokemon)

    return render(
        request,
        "pokemoncitos/formulario_pokemon.html",
        {"formulario": formulario}
    )


# ELIMINAR UN POKEMON
@rol_requerido("ADMIN")
def eliminar_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)

    if request.method == "POST":
        pokemon.delete()
        return redirect("inicio")

    return render(
        request,
        "pokemoncitos/confirmar_eliminar.html",
        {"pokemon": pokemon}
    )


# REGISTRAR UN GIMNASIO
@rol_requerido("ADMIN", "EDITOR")
def crear_gimnasio(request):
    if request.method == "POST":
        formulario = GimnasioForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = GimnasioForm()

    return render(
        request,
        "pokemoncitos/formulario_gimnasio.html",
        {"formulario": formulario}
    )


# EDITAR UN GIMNASIO
@rol_requerido("ADMIN", "EDITOR")
def editar_gimnasio(request, id):
    gimnasio = get_object_or_404(Gimnasio, id=id)

    if request.method == "POST":
        formulario = GimnasioForm(
            request.POST,
            instance=gimnasio
        )

        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = GimnasioForm(instance=gimnasio)

    return render(
        request,
        "pokemoncitos/formulario_gimnasio.html",
        {"formulario": formulario}
    )


# ELIMINAR UN GIMNASIO
@rol_requerido("ADMIN")
def eliminar_gimnasio(request, id):
    gimnasio = get_object_or_404(Gimnasio, id=id)

    if request.method == "POST":
        gimnasio.delete()
        return redirect("inicio")

    return render(
        request,
        "pokemoncitos/confirmar_eliminar_gimnasio.html",
        {"gimnasio": gimnasio}
    )


# REGISTRAR UN ENTRENADOR
@rol_requerido("ADMIN", "EDITOR")
def crear_entrenador(request):
    if request.method == "POST":
        formulario = EntrenadorForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = EntrenadorForm()

    return render(
        request,
        "pokemoncitos/formulario_entrenador.html",
        {"formulario": formulario}
    )


# EDITAR UN ENTRENADOR
@rol_requerido("ADMIN", "EDITOR")
def editar_entrenador(request, id):
    entrenador = get_object_or_404(Entrenador, id=id)

    if request.method == "POST":
        formulario = EntrenadorForm(
            request.POST,
            instance=entrenador
        )

        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = EntrenadorForm(instance=entrenador)

    return render(
        request,
        "pokemoncitos/formulario_entrenador.html",
        {"formulario": formulario}
    )


# ELIMINAR UN ENTRENADOR
@rol_requerido("ADMIN")
def eliminar_entrenador(request, id):
    entrenador = get_object_or_404(Entrenador, id=id)

    if request.method == "POST":
        entrenador.delete()
        return redirect("inicio")

    return render(
        request,
        "pokemoncitos/confirmar_eliminar_entrenador.html",
        {"entrenador": entrenador}
    )



# POKEDEX CON POKEAPI
import requests


def pokedex(request):
    nombre = request.GET.get("nombre", "").strip().lower()
    pokemon_api = None
    error = None

    if nombre:
        try:
            respuesta = requests.get(
                f"https://pokeapi.co/api/v2/pokemon/{nombre}",
                timeout=10
            )

            if respuesta.status_code == 200:
                datos = respuesta.json()

                pokemon_api = {
                    "nombre": datos["name"].capitalize(),
                    "imagen": datos["sprites"]["other"]["official-artwork"]["front_default"],
                    "altura": datos["height"] / 10,
                    "peso": datos["weight"] / 10,
                    "tipos": [
                        tipo["type"]["name"]
                        for tipo in datos["types"]
                    ],
                    "habilidades": [
                        habilidad["ability"]["name"]
                        for habilidad in datos["abilities"]
                    ],
                    "experiencia": datos["base_experience"],
                    "estadisticas": [
                        {
                            "nombre": estadistica["stat"]["name"],
                            "valor": estadistica["base_stat"]
                        }
                        for estadistica in datos["stats"]
                    ]
                }
            else:
                error = "No encontramos ese Pokémon. Revisa el nombre."

        except requests.RequestException:
            error = "No pudimos conectar con PokéAPI. Inténtalo de nuevo."

    return render(
        request,
        "pokemoncitos/pokedex.html",
        {
            "pokemon_api": pokemon_api,
            "error": error,
            "nombre": nombre
        }
    )


