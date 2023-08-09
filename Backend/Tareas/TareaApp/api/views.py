from rest_framework import viewsets
from TareaApp.models import Tarea
from TareaApp.api.serializers import TareaSerializer

# Creo un modelo de vista
class TareaViewSet( viewsets.ModelViewSet ):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer