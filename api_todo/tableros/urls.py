from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TareasViewSet, TareasByIdViewSet


router = DefaultRouter()
router.register(r'tareas', TareasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tareas/<int:id>', TareasByIdViewSet.as_view({'get': 'list'})),
]
