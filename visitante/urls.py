# visitante/urls.py
from django.urls import path
from .views import VisitanteHomeView

app_name = 'visitante'

urlpatterns = [
    path('home/', VisitanteHomeView.as_view(), name='home'),
    # ... más patrones de URL ...
]

