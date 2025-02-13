
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template import loader
from .views import inicio_view, bienvenida_view, contenido_view
from django.conf import settings
from django.conf.urls.static import static


def inicio_view(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render({}, request))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name='inicio'),
    path('bienvenida/', bienvenida_view, name='bienvenida'),
    path('contenido/', contenido_view, name='contenido'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)