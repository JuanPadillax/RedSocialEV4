from django.shortcuts import render


def CrearPelicula(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        destino = request.POST.get('director')
        texto = request.POST.get('año_lanzamiento')
        fecha = request.POST.get('genero')
        Movies.objects.create(titulo=titulo, director=director,
                              año_lanzamiento=año_lanzamiento, genero=genero)
        return redirect('listar_peliculas')
    print(Movies)
    return render(request, 'index.html')
