from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'number_of_players', 'number_of_games', 'format']
