from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Añade los campos de radio con las nuevas opciones
    user_type = forms.ChoiceField(
        choices=[
            ('is_administrador', 'Administrador'), 
            ('is_alumno', 'Alumno'),
            ('is_visitante', 'Visitante'),  # Nueva opción
            ('is_docente', 'Docente')  # Nueva opción
        ],
        widget=forms.RadioSelect
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('user_type',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data['user_type']

        # Resetea los estados a False para manejar múltiples tipos
        user.is_administrador = False
        user.is_alumno = False
        user.is_visitante = False  # Asegúrate de tener este campo en tu modelo
        user.is_docente = False  # Asegúrate de tener este campo en tu modelo

        if user_type == 'is_administrador':
            user.is_administrador = True
        elif user_type == 'is_alumno':
            user.is_alumno = True
        elif user_type == 'is_visitante':  # Nueva condición
            user.is_visitante = True
        elif user_type == 'is_docente':  # Nueva condición
            user.is_docente = True

        if commit:
            user.save()
        return user
