from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('', views.inicio, name='inicio'),  # Asumimos que esta ya existe
]