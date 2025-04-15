from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    
    path('', views.inicio, name='inicio'),  

    path('nosotros/', views.nosotros, name='nosotros'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('faq/', views.faq, name='faq'),
    path('glnchile/', views.glnchile, name='glnchile'),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
    path('noticias/', views.noticias, name='noticias'),
]