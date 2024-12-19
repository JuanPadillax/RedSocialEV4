from django.urls import path
from publicaciones.views import crear_publicacion, listar_publicaciones, actualizar_publicaciones, eliminar_publicaciones

urlpatterns = [
    path('listar_publicaciones/', listar_publicaciones,
         name='listar_publicaciones'),
    path('crear_publicacion/', crear_publicacion, name='crear_publicacion'),
    path('actualizar_publicacion/<int:id>/',
         actualizar_publicaciones, name='actualizar_publicacion'),
    path('eliminar_publicacion/<int:id>/',
         eliminar_publicaciones, name='eliminar_publicacion'),

]
