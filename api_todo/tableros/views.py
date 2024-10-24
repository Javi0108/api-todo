from rest_framework import viewsets
from .models import Tareas
from .serializers import TareasSerializer

class TareasViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

class TareasByIdViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        return Tareas.objects.filter(id=id)
