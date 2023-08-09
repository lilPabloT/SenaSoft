from django.contrib import admin
from TareaApp.models import Tarea

# Register your models here.

class TareaAdmin( admin.ModelAdmin ):
    list_display = ['id', 'titulo']

admin.site.register(Tarea, TareaAdmin)