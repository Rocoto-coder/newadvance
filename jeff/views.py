from django.shortcuts import render
import random


def inicio_view(request):
    return render(request, 'inicio.html')

def bienvenida_view(request):
    stars = [
        {
            'top': random.randint(0, 100),
            'left': random.randint(0, 100),
            'delay': random.uniform(0, 2)
        }
        for _ in range(100)
    ]
    context = {
        'stars': stars
    }
    return render(request, 'bienvenida.html', context)

def contenido_view(request):
    return render(request, 'contenido.html')

