from .models import Publicacion, Destino
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion
from destinos.models import Destino
from django.utils.timezone import now
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from .models import Publicacion
from .serializers import PublicacionSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView


@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        destino_id = request.POST.get('destino')
        texto = request.POST.get('texto')

        if not texto or len(texto.strip()) < 10:
            destinos = Destino.objects.all()
            error = "El texto debe tener al menos 10 caracteres."
            return render(request, 'crear_publicacion.html', {'destinos': destinos, 'error': error})

        try:
            destino = get_object_or_404(Destino, id=destino_id)
        except ValueError:
            destinos = Destino.objects.all()
            error = "El destino seleccionado no es válido."
            return render(request, 'crear_publicacion.html', {'destinos': destinos, 'error': error})

        Publicacion.objects.create(
            usuario=request.user,
            destino=destino,
            texto=texto,
            fecha=now().date()
        )
        return redirect('listar_publicaciones')

    destinos = Destino.objects.all()
    return render(request, 'crear_publicacion.html', {'destinos': destinos})


@login_required
def listar_publicaciones(request):
    publicaciones_list = Publicacion.objects.all().order_by('-fecha')
    paginator = Paginator(publicaciones_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listar_publicaciones.html', {'page_obj': page_obj})


@login_required
def actualizar_publicaciones(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)

    if request.method == 'POST':
        destino_id = request.POST.get('destino')
        texto = request.POST.get('texto')

        destino = get_object_or_404(Destino, id=destino_id)

        if not texto or len(texto.strip()) < 10:
            return render(request, 'actualizar_publicacion.html', {
                'publicacion': publicacion,
                'destinos': Destino.objects.all(),
                'error': 'El texto debe tener al menos 10 caracteres.'
            })

        publicacion.destino = destino
        publicacion.texto = texto
        publicacion.fecha = now().date()
        publicacion.save()
        return redirect('listar_publicaciones')

    destinos = Destino.objects.all()
    return render(request, 'actualizar_publicacion.html', {
        'publicacion': publicacion,
        'destinos': destinos
    })


@login_required
def eliminar_publicaciones(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('listar_publicaciones')
    return render(request, 'eliminar_publicacion.html', {'publicacion': publicacion})


class PublicacionPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class PublicacionListCreateView(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    pagination_class = PublicacionPagination
    permission_classes = [permissions.IsAuthenticated]


class PublicacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublicacionListCreateView(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    pagination_class = PublicacionPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['usuario__username', 'destino__ciudad', 'destino__pais']


class PublicacionListAPIView(ListAPIView):
    queryset = Publicacion.objects.all().order_by('-fecha')
    serializer_class = PublicacionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PublicacionPagination
