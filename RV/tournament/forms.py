from django import forms
from .models import Tournament, Player, Game

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'number_of_players', 'number_of_games', 'format']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name']
