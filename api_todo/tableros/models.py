from django.db import models

class Tableros(models.Model):
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class Listas(models.Model):
    nombre = models.CharField(max_length=100)
    tablero = models.ForeignKey(Tableros, related_name='listas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Tareas(models.Model):
    descripcion = models.TextField(blank=True, null=True)
    lista = models.ForeignKey(Listas, related_name='tareas', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion
