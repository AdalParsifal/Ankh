from django.http import HttpResponseForbidden

def requiere_grado(minimo):
    orden = ['visitante', 'aprendiz', 'compañero', 'maestro']

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Debes iniciar sesión.")
            grado_usuario = request.user.perfilusuario.grado
            if orden.index(grado_usuario) >= orden.index(minimo):
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("No tienes permiso para acceder a esta sección.")
        return _wrapped_view
    return decorator