from django.contrib import admin
from .models import Publicacion, Noticia

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo',)
    list_filter = ('fecha_publicacion',)
    ordering = ('-fecha_publicacion',)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'autor')
    search_fields = ('titulo', 'contenido')
    list_filter = ('fecha_publicacion',)
