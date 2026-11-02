
from django import forms
from .models import Pokemon, Gimnasio,Entrenador


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon

        fields = [
            "nombre",
            "peso",
            "imagen",
            "entrenador",
            "habilidades",
            "naturaleza",
            "elemento",
            "descripcion",
            "color_carta",
            "accesorio",
        ]

        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 3}),
            "habilidades": forms.Textarea(attrs={"rows": 3}),
        }
        
class GimnasioForm(forms.ModelForm):

    class Meta:
        model = Gimnasio

        fields = [
            "nombre",
            "elemento",
            "insignia",
            "lider",
        ]

        
class EntrenadorForm(forms.ModelForm):

    class Meta:
        model = Entrenador

        fields = [
            "documento",
            "nombre",
            "apellido",
            "medallas",
        ]


