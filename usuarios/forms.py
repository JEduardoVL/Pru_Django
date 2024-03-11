from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Añade los campos de radio
    user_type = forms.ChoiceField(
        choices=[('is_administrador', 'Administrador'), ('is_alumno', 'Alumno')],
        widget=forms.RadioSelect
    )
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('user_type',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data['user_type']
        if user_type == 'is_administrador':
            user.is_administrador = True
        elif user_type == 'is_alumno':
            user.is_alumno = True
        if commit:
            user.save()
        return user
