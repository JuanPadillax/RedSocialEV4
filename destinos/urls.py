from django.urls import path
from destinos.views import crear_destino, listar_destinos, actualizar_destino, eliminar_destino

urlpatterns = [
    path('listar_destinos', listar_destinos, name='listar_destinos'),
    path('crear_destino/', crear_destino, name='crear_destino'),
    path('actualizar_destino/<int:id>/', actualizar_destino,
         name='actualizar_destino'),
    path('eliminar_destino/<int:id>/', eliminar_destino,
         name='eliminar_destino')

]
