
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template import loader
from .views import inicio_view, bienvenida_view, contenido_view


def inicio_view(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render({}, request))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name='inicio'),
    path('bienvenida/', bienvenida_view, name='bienvenida'),
    path('contenido/', contenido_view, name='contenido'),
]
