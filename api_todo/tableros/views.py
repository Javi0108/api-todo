from rest_framework import viewsets
from .models import Tableros, Listas, Tareas
from .serializers import TablerosSerializer, ListasSerializer, TareasSerializer


# Tableros ViewSet
class TablerosViewSet(viewsets.ModelViewSet):
    queryset = Tableros.objects.all()
    serializer_class = TablerosSerializer

# Tableros por ID
class TablerosByIdViewSet(viewsets.ModelViewSet):
    queryset = Tableros.objects.all()
    serializer_class = TablerosSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')  # Obtenemos el ID desde los kwargs
        return Tableros.objects.filter(id=id)

# Listas ViewSet
class ListasViewSet(viewsets.ModelViewSet):
    queryset = Listas.objects.all()
    serializer_class = ListasSerializer

# Listas por ID
class ListasByIdViewSet(viewsets.ModelViewSet):
    queryset = Listas.objects.all()
    serializer_class = ListasSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        return Listas.objects.filter(id=id)

# Listas por ID del tablero
class ListasByTableroIdViewSet(viewsets.ModelViewSet):
    queryset = Listas.objects.all()
    serializer_class = ListasSerializer

    def get_queryset(self):
        tablero = self.kwargs.get('tablero')
        return Listas.objects.filter(tablero=tablero)

class TareasViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

class TareasByIdViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        return Tareas.objects.filter(id=id)
    
class TareasByListaIdViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

    def get_queryset(self):
        lista = self.kwargs.get('lista')
        return Tareas.objects.filter(lista=lista)