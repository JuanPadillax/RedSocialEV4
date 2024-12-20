from django.urls import path
from publicaciones.views import crear_publicacion, listar_publicaciones, actualizar_publicaciones, eliminar_publicaciones, PublicacionListCreateView, PublicacionDetailView, PublicacionListAPIView

urlpatterns = [
    path('api/publicaciones/', PublicacionListAPIView.as_view(), name='publicaciones'),
    path('api/publicaciones/', PublicacionListCreateView.as_view(),
         name='publicaciones'),
    path('api/publicaciones/<int:pk>/',
         PublicacionDetailView.as_view(), name='publicacion_detail'),
    path('listar_publicaciones/', listar_publicaciones,
         name='listar_publicaciones'),
    path('crear_publicacion/', crear_publicacion, name='crear_publicacion'),
    path('actualizar_publicacion/<int:id>/',
         actualizar_publicaciones, name='actualizar_publicacion'),
    path('eliminar_publicacion/<int:id>/',
         eliminar_publicaciones, name='eliminar_publicacion'),

]
