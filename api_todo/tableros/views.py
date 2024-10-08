from rest_framework import viewsets
from .models import Tableros, Listas, Tareas
from .serializers import TablerosSerializer, ListasSerializer, TareasSerializer

class TablerosViewSet(viewsets.ModelViewSet):
    queryset = Tableros.objects.all()
    serializer_class = TablerosSerializer

class ListasViewSet(viewsets.ModelViewSet):
    queryset = Listas.objects.all()
    serializer_class = ListasSerializer

class TareasViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
