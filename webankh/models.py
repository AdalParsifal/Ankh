from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    GRADOS = [
        ('visitante', 'Visitante'),
        ('aprendiz', 'Aprendiz'),
        ('compañero', 'Compañero'),
        ('maestro', 'Maestro'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    grado = models.CharField(max_length=20, choices=GRADOS, default='visitante')

    def __str__(self):
        return f"{self.usuario.username} ({self.get_grado_display()})"

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(usuario=instance)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contenido = models.TextField(help_text="Puedes usar HTML o Markdown.")
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    imagen_destacada = models.ImageField(upload_to='publicaciones/', null=True, blank=True)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo


