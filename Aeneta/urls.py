from django.contrib import admin
from django.urls import path, include
from usuarios.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Incluye las URLs de la aplicación usuarios
    path('', CustomLoginView.as_view(), name='login'),  # El path vacío redirige al login
    path('administracion/', include('administracion.urls', namespace='administracion')),  # Incluye las URLs con el namespace
    path('alumnos/', include('alumnos.urls', namespace='alumnos')),
   
    # ... cualquier otra ruta que necesites ...
]
