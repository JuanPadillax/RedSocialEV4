from django.shortcuts import render, redirect
from .models import Destino
from django.contrib.auth.decorators import login_required


def crear_destino(request):
    if request.method == 'POST':
        pais = request.POST.get('pais')
        ciudad = request.POST.get('ciudad')
        descripcion = request.POST.get('descripcion')

        Destino.objects.create(pais=pais, ciudad=ciudad,
                               descripcion=descripcion)
        return redirect('listar_destinos')
    return render(request, 'crear_destino.html')


@login_required
def listar_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'listar_destinos.html', {'destinos': destinos})


@login_required
def actualizar_destino(request, id):
    destino = Destino.objects.get(id=id)
    if request.method == 'POST':
        destino.pais = request.POST.get('pais')
        destino.ciudad = request.POST.get('ciudad')
        destino.descripcion = request.POST.get('descripcion')
        destino.save()
        return redirect('listar_destinos')
    return render(request, 'actualizar_destino.html', {'destino': destino})


@login_required
def eliminar_destino(request, id):
    destino = Destino.objects.get(id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('listar_destinos')
    return render(request, 'eliminar_destino.html', {'destino': destino})
