from django.contrib.auth.models import AbstractUser
from django.db import models

# Creación de los tipos de usuario
class CustomUser(AbstractUser):
    is_administrador = models.BooleanField(default=False)
    is_alumno = models.BooleanField(default=False)
    #is_visitante = models.BooleanField(default=False)  
    is_docente = models.BooleanField(default=False) 
