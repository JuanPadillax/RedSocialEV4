from .models import Publicacion, Destino
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion
from destinos.models import Destino
from django.utils.timezone import now


@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        destino_id = request.POST.get('destino')  # ID del destino seleccionado
        texto = request.POST.get('texto')

        # Verifica que el destino exista en la base de datos
        destino = get_object_or_404(Destino, id=destino_id)

        # Crear la publicación con la fecha de hoy
        Publicacion.objects.create(
            usuario=request.user,  # Usuario autenticado
            destino=destino,
            texto=texto,
            fecha=now().date()  # Fecha de hoy sin hora
        )
        return redirect('listar_publicaciones')

    # Mostrar todos los destinos disponibles
    destinos = Destino.objects.all()
    return render(request, 'crear_publicacion.html', {'destinos': destinos})


@login_required
def listar_publicaciones(request):
    publi = Publicacion.objects.all()
    return render(request, 'listar_publicaciones.html', {'publi': publi})


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
        publicacion.fecha = now().date()  # Asegúrate de guardar solo la fecha
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
