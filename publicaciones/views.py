from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion


def crear_publicacion(request):
    if request.method == 'POST':
        destino = request.POST.get('destino')
        texto = request.POST.get('texto')
        fecha = request.POST.get('fecha')
        Publicacion.objects.create(destino=destino,
                                   texto=texto, fecha=fecha)
        return redirect('listar_publicaciones')
    return render(request, 'crear_publicacion.html')


def listar_publicaciones(request):
    publi = Publicacion.objects.all()
    return render(request, 'listar_publicaciones.html', {'publi': publi})


def actualizar_publicaciones(request, id):
    publi = get_object_or_404(Publicacion, id=id)
    if request.method == 'POST':
        publi.usuario = request.POST.get('usuario')
        publi.destino = request.POST.get('destino')
        publi.texto = request.POST.get('texto')
        publi.fecha = request.POST.get('fecha')
        publi.save()
        return redirect('listar_publicaciones')
    return render(request, 'actualizar_publicaciones.html', {'publi': publi})


def eliminar_publicaciones(request, id):
    publi = get_object_or_404(Publicacion, id=id)
    if request.method == 'POST':
        publi.delete()
        return redirect('listar_publicaciones')
    return render(request, 'eliminar_publicaciones.html', {'publi': publi})
