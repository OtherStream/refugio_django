from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),
    
    # Rutas de tus apps
    path('animales/', include('animales.urls')),
    path('adopciones/', include('adopciones.urls')),
    path('productos/', include('productos.urls')),
    path('servicios/', include('servicios.urls')),
    path('avisos/', include('avisos.urls')),
    
    # Rutas de autenticación (login, registro)
    path('auth/', include('usuarios.urls')),
    
    # Rutas principales (core) - ¡Debe ir al final!
    path('', include('core.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)