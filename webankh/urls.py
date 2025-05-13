from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    
    path('', views.inicio, name='inicio'),  

    path('nosotros/', views.nosotros, name='nosotros'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('faq/', views.faq, name='faq'),
    path('glnchile/', views.glnchile, name='glnchile'),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
    path('noticias/', views.noticias, name='noticias'),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    path('panel/', views.panel_admin, name='panel_admin'),
    path('panel/aprobar/<int:user_id>/', views.aprobar_usuario, name='aprobar_usuario'),
]