from rest_framework import viewsets
from .models import Tableros, Listas, Tareas
from .serializers import TablerosSerializer, ListasSerializer, TareasSerializer
from rest_framework.exceptions import NotFound
from rest_framework.response import Response



class TablerosViewSet(viewsets.ModelViewSet):
    queryset = Tableros.objects.all()
    serializer_class = TablerosSerializer

class TablerosByIdViewSet(viewsets.ModelViewSet):
    serializer_class = TablerosSerializer

    def list(self, request, tablero_id):
        if not tablero_id:
            raise NotFound("El parámetro 'tablero_id' es requerido.")
        try:
            id = Tableros.objects.filter(tablero__id=tablero_id)  # Filtra por tablero_id
            serializer = self.serializer_class(id, many=True)
            return Response(serializer.data)
        except Tableros.DoesNotExist:
            raise NotFound(f"No se encontró el tablero con id {tablero_id}")

class ListasViewSet(viewsets.ModelViewSet):
    queryset = Listas.objects.all()
    serializer_class = ListasSerializer

    def get_queryset(self):
        tablero_id = self.request.query_params.get('tablero_id')  # Obtenemos el tablero_id de los query params
        if tablero_id:
            try:
                return Listas.objects.filter(tablero__id=tablero_id)  # Filtramos las listas por el id del tablero
            except Tableros.DoesNotExist:
                raise NotFound(f"No se encontró un tablero con el id {tablero_id}")
        else:
            raise NotFound("El parámetro 'tablero_id' es requerido.")

class TareasViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
