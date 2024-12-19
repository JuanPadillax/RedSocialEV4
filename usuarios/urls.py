from django.urls import path
from usuarios.views import crear_usuario, listar_usuarios, actualizar_usuario, eliminar_usuario

urlpatterns = [
    path('', listar_usuarios, name='listar_usuarios'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('actualizar_usuario/<int:id>/', actualizar_usuario,
         name='actualizar_usuario'),
    path('eliminar_usuario/<int:id>/', eliminar_usuario,
         name='eliminar_usuario')
]
