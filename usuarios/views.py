from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        User.objects.create_user(
            username=username, email=email, password=password)
        return redirect('listar_usuarios')
    return render(request, 'crear_usuario.html')


@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})


@login_required
def actualizar_usuario(request, id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        usuario.email = request.POST.get('email')
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'actualizar_usuario.html', {'usuario': usuario})


@login_required
def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})
