from django.urls import path
from .views import leaderboard_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('leaderboard', leaderboard_view, name='leaderboard'),
    # Autres URLs de votre application...
]