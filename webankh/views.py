from django.shortcuts import render, redirect

def bienvenida(request):
    if request.method == 'POST':
        es_mason = request.POST.get('es_mason') == 'si'
        idioma = request.POST.get('idioma')

        request.session['es_mason'] = es_mason
        request.session['idioma'] = idioma

        return redirect('inicio')  # Asumimos que tenés una vista "inicio"

    return render(request, 'bienvenida.html')

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def publicaciones(request):
    return render(request, 'publicaciones.html')

def faq(request):
    return render(request, 'faq.html')

def glnchile(request):
    return render(request, 'glnchile.html')

def biblioteca(request):
    return render(request, 'biblioteca.html')

def noticias(request):
    return render(request, 'noticias.html')