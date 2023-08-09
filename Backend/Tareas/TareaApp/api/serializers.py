from rest_framework import serializers
from TareaApp.models import Tarea


# Creo el serializado en el que paso los parametros de la api
class TareaSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'texto', 'estado' ]