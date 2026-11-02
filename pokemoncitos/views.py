
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pokemon, Gimnasio, Entrenador
from .forms import PokemonForm,GimnasioForm,EntrenadorForm


def inicio(request):
    pokemones = Pokemon.objects.all()
    gimnasios = Gimnasio.objects.all()
    entrenadores = Entrenador.objects.all()

    contexto = {
        "pokemones": pokemones,
        "gimnasios": gimnasios,
        "entrenadores": entrenadores,
    }

    return render(request, "pokemoncitos/inicio.html", contexto)


# REGISTRAR UN POKEMON
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


