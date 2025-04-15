from django.shortcuts import redirect

class CheckBienvenidaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/bienvenida/') and not request.session.get('idioma'):
            return redirect('bienvenida')
        return self.get_response(request)