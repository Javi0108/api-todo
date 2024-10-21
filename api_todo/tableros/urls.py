from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TablerosViewSet, TablerosByIdViewSet, ListasViewSet, ListasByIdViewSet, ListasByTableroIdViewSet, TareasViewSet, TareasByIdViewSet, TareasByListaIdViewSet


router = DefaultRouter()
router.register(r'tableros', TablerosViewSet, basename='tableros')
router.register(r'listas', ListasViewSet)
router.register(r'tareas', TareasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tableros/<int:id>', TablerosByIdViewSet.as_view({'get': 'list'})),
    path('listas/<int:id>', ListasByIdViewSet.as_view({'get': 'list'})),
    path('listas/tablero/<int:tablero>', ListasByTableroIdViewSet.as_view({'get': 'list'})),
    path('tareas/<int:id>', TareasByIdViewSet.as_view({'get': 'list'})),
    path('tareas/lista/<int:lista>', TareasByListaIdViewSet.as_view({'get': 'list'})),
]
