
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def rol_requerido(*roles_permitidos):
    def decorador(vista):
        @wraps(vista)
        @login_required
        def vista_protegida(request, *args, **kwargs):

            # El superusuario tiene acceso administrativo
            if request.user.is_superuser:
                return vista(request, *args, **kwargs)

            # Comprobar que el usuario tenga perfil
            try:
                perfil = request.user.perfil
            except ObjectDoesNotExist:
                messages.error(
                    request,
                    "Tu usuario no tiene un perfil asignado."
                )
                return redirect("inicio")

            # Comprobar si el rol está autorizado
            if perfil.rol in roles_permitidos:
                return vista(request, *args, **kwargs)

            messages.error(
                request,
                "No tienes permisos para realizar esta acción."
            )
            return redirect("inicio")

        return vista_protegida

    return decorador
