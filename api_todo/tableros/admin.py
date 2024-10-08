from django.contrib import admin
from .models import Tableros, Listas, Tareas

# Personaliza la vista del modelo Tarea
class TareasAdmin(admin.ModelAdmin):
    list_display = ['descripcion','completada', 'lista', 'fecha_creacion']  # Campos a mostrar en la lista del admin
    list_filter = ['completada', 'lista']  # Filtros laterales en la vista de administración
    search_fields = ['descripcion']  # Búsqueda por título

# Personaliza la vista del modelo Lista
class ListasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tablero']
    search_fields = ['nombre']

# Personaliza la vista del modelo Tablero
class TablerosAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'fecha_creacion']
    search_fields = ['descripcion']

# Registrar los modelos en el administrador
admin.site.register(Tareas, TareasAdmin)
admin.site.register(Listas, ListasAdmin)
admin.site.register(Tableros, TablerosAdmin)