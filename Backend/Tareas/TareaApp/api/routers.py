from rest_framework import routers
from TareaApp.api.views import TareaViewSet

# Creo el router para pasarlo a las urls
router = routers.DefaultRouter()
router.register( prefix = 'tareas', basename = 'tareas', viewset = TareaViewSet )