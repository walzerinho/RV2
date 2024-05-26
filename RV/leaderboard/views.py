from django.shortcuts import render
from .models import Leaderboard

def leaderboard_view(request):
    leaderboard = Leaderboard.objects.all()
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})

def home_view(request):
    return render(request, 'home.html')