from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TablerosViewSet, ListasViewSet, TareasViewSet


router = DefaultRouter()
router.register(r'tableros', TablerosViewSet, basename='tableros')
router.register(r'listas', ListasViewSet)
router.register(r'tareas', TareasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
