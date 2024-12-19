from django.urls import path
from publicaciones.views import crear_publicacion, listar_publicaciones, actualizar_publicaciones, eliminar_publicaciones

urlpatterns = [
    path('', listar_publicaciones, name='lista_publicaciones'),
    path('crear_publicacion/', crear_publicacion, name='crear_publicacion'),
    path('actualizar_publicaciones/<int:id>/',
         actualizar_publicaciones, name='actualizar_publicaciones'),
    path('eliminar_publicaciones/<int:id>/',
         eliminar_publicaciones, name='eliminar_publicaciones'),

]
