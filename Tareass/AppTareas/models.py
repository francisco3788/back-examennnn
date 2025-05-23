from django.db import models

class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('hecha', 'Hecha'),
        ('cancelada', 'Cancelada'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
