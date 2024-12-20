from rest_framework import generics, permissions
from .serializers import DestinoSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Destino
from django.contrib.auth.decorators import login_required


def crear_destino(request):
    if request.method == 'POST':
        pais = request.POST.get('pais')
        ciudad = request.POST.get('ciudad')
        descripcion = request.POST.get('descripcion')

        if not pais or not ciudad or not descripcion:
            return render(request, 'crear_destino.html', {'error': 'Todos los campos son obligatorios.'})

        destino = Destino(pais=pais, ciudad=ciudad, descripcion=descripcion)
        destino.save()
        return redirect('listar_destinos')

    return render(request, 'crear_destino.html')


@login_required
def listar_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'listar_destinos.html', {'destinos': destinos})


@login_required
def actualizar_destino(request, id):
    destino = get_object_or_404(Destino, id=id)
    if request.method == 'POST':
        pais = request.POST.get('pais')
        ciudad = request.POST.get('ciudad')
        descripcion = request.POST.get('descripcion')

        if not pais or not ciudad or not descripcion:
            return render(request, 'actualizar_destino.html', {'destino': destino, 'error': 'Todos los campos son obligatorios.'})

        destino.pais = pais
        destino.ciudad = ciudad
        destino.descripcion = descripcion
        destino.save()
        return redirect('listar_destinos')

    return render(request, 'actualizar_destino.html', {'destino': destino})


@login_required
def eliminar_destino(request, id):
    destino = get_object_or_404(Destino, id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('listar_destinos')
    return render(request, 'eliminar_destino.html', {'destino': destino})


class DestinoListCreateView(generics.ListCreateAPIView):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    permission_classes = [permissions.IsAuthenticated]


class DestinoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    permission_classes = [permissions.IsAuthenticated]
