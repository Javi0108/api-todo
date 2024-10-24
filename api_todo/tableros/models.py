from django.db import models

class Tareas(models.Model):
    descripcion = models.TextField(blank=True, null=True)
    fecha_fin = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.descripcion} - {self.fecha_fin.strftime('%d/%m/%Y')}"
