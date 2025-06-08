from django.shortcuts import render, redirect
from .models import Publicacion, Noticia, PerfilUsuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import LoginForm

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
    publicaciones = Publicacion.objects.all()
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})

def faq(request):
    return render(request, 'faq.html')

def glnchile(request):
    return render(request, 'glnchile.html')

def biblioteca(request):
    return render(request, 'biblioteca.html')

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # ← Espera aprobación
            user.save()
            # PerfilUsuario.objects.create(usuario=user) # NO crear el perfil manualmente, ya lo hace el signal
            return render(request, 'registro_enviado.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'

@login_required
def perfil(request):
    perfil = request.user.perfilusuario
    return render(request, 'perfil.html', {'perfil': perfil})

@staff_member_required
def panel_admin(request):
    pendientes = User.objects.filter(is_active=False)
    usuarios = User.objects.filter(is_active=True).order_by('date_joined')
    return render(request, 'panel_admin.html', {'pendientes': pendientes, 'usuarios': usuarios})

@staff_member_required
def aprobar_usuario(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('panel_admin')