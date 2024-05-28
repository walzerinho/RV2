from django.urls import path
from .views import create_tournament

urlpatterns = [
    path('create_tournament', create_tournament, name='create_tournament'),
    # Autres URLs de votre application...
]