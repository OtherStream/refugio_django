from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de tus apps
    path('', include('core.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('animales/', include('animales.urls')),
    path('adopciones/', include('adopciones.urls')),
    path('productos/', include('productos.urls')),
    path('servicios/', include('servicios.urls')),
    path('avisos/', include('avisos.urls')),
    path('', include('core.urls')),
]
