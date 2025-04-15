from django.shortcuts import render, redirect

def bienvenida(request):
    if request.method == 'POST':
        es_mason = request.POST.get('es_mason') == 'si'
        idioma = request.POST.get('idioma')

        request.session['es_mason'] = es_mason
        request.session['idioma'] = idioma

        return redirect('inicio')  # Asumimos que tenés una vista "inicio"

    return render(request, 'bienvenida.html')
