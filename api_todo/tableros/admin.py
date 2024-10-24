from django.contrib import admin
from .models import Tareas

# Personaliza la vista del modelo Tarea
class TareasAdmin(admin.ModelAdmin):
    list_display = ['descripcion','completada', 'fecha_fin', 'fecha_creacion']
    list_filter = ['completada', 'descripcion']
    search_fields = ['descripcion'] 

# Registrar los modelos en el administrador
admin.site.register(Tareas, TareasAdmin)