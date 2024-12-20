from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import crear_usuario, listar_usuarios, actualizar_usuario, eliminar_usuario, UserListView

urlpatterns = [
    path('api/usuarios/', UserListView.as_view(), name='usuarios'),
    path('', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('actualizar_usuario/<int:id>/', actualizar_usuario,
         name='actualizar_usuario'),
    path('eliminar_usuario/<int:id>/', eliminar_usuario,
         name='eliminar_usuario')
]
