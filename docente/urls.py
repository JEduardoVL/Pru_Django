# docente/urls.py
from django.urls import path
from .views import DocenteHomeView

app_name = 'docente'

urlpatterns = [
    path('home/', DocenteHomeView.as_view(), name='home'),
    # ... más patrones de URL ...
]

