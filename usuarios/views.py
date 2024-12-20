from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import login
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer


def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or len(username.strip()) < 5:
            return render(request, 'crear_usuario.html', {'error': 'El nombre de usuario debe tener al menos 5 caracteres.'})
        if not email:
            return render(request, 'crear_usuario.html', {'error': 'El correo electrónico es obligatorio.'})
        if not password or len(password) < 8:
            return render(request, 'crear_usuario.html', {'error': 'La contraseña debe tener al menos 8 caracteres.'})

        try:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            login(request, user)
            return redirect('listar_usuarios')
        except IntegrityError:
            return render(request, 'crear_usuario.html', {'error': 'El nombre de usuario ya está en uso.'})

    return render(request, 'crear_usuario.html')


@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})


@login_required
def actualizar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        email = request.POST.get('email')

        if not email:
            return render(request, 'actualizar_usuario.html', {'usuario': usuario, 'error': 'El correo electrónico es obligatorio.'})

        usuario.email = email
        usuario.save()
        return redirect('listar_usuarios')

    return render(request, 'actualizar_usuario.html', {'usuario': usuario})


@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
