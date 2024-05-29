from django.urls import path
from .views import create_tournament, tournament_details

urlpatterns = [
    path('create_tournament', create_tournament, name='create_tournament'),
    path('tournament/<int:pk>/', tournament_details, name='tournament_details'),
]