from rest_framework import serializers
from .models import Tableros, Listas, Tareas

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'

class ListasSerializer(serializers.ModelSerializer):
    tareas = TareasSerializer(many=True, read_only=True)

    class Meta:
        model = Listas
        fields = '__all__'

class TablerosSerializer(serializers.ModelSerializer):
    listas = ListasSerializer(many=True, read_only=True)

    class Meta:
        model = Tableros
        fields = '__all__'
