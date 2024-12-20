from django.urls import path
from destinos.views import crear_destino, listar_destinos, actualizar_destino, eliminar_destino, DestinoListCreateView, DestinoDetailView

urlpatterns = [
    path('api/destinos/', DestinoListCreateView.as_view(), name='destinos'),
    path('api/destinos/<int:pk>/',
         DestinoDetailView.as_view(), name='destino_detail'),
    path('listar_destinos', listar_destinos, name='listar_destinos'),
    path('crear_destino/', crear_destino, name='crear_destino'),
    path('actualizar_destino/<int:id>/', actualizar_destino,
         name='actualizar_destino'),
    path('eliminar_destino/<int:id>/', eliminar_destino,
         name='eliminar_destino')

]
