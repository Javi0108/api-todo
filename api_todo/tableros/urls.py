from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TablerosViewSet, TablerosByIdViewSet, ListasViewSet, ListasByIdViewSet, TareasViewSet


router = DefaultRouter()
router.register(r'tableros', TablerosViewSet, basename='tableros')
router.register(r'listas', ListasViewSet)
router.register(r'tareas', TareasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tableros/<int:id>', TablerosByIdViewSet.as_view({'get': 'list'})),
    path('listas/tablero/<int:tablero>', ListasByIdViewSet.as_view({'get': 'list'})),

]
