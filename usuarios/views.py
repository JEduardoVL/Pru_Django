from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/signup.html'

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'  # Especifica la ubicación del template

    def get_success_url(self):
        # Lógica para redirigir a diferentes usuarios a diferentes páginas
        if self.request.user.is_administrador:
            return resolve_url('administracion:home')
        elif self.request.user.is_alumno:
            return resolve_url('alumnos:home')
        else:
            return resolve_url('tu_url_por_defecto')