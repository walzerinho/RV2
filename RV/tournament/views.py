from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .forms import TournamentForm, PlayerForm, GameForm
from .models import Tournament, Player, Game

def create_tournament(request):
    PlayerFormSet = modelformset_factory(Player, form=PlayerForm, extra=0)
    GameFormSet = modelformset_factory(Game, form=GameForm, extra=0)
    
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        player_formset = PlayerFormSet(request.POST, queryset=Player.objects.none(), prefix='players')
        game_formset = GameFormSet(request.POST, queryset=Game.objects.none(), prefix='games')
        
        if form.is_valid() and player_formset.is_valid() and game_formset.is_valid():
            tournament = form.save()
            for player_form in player_formset:
                player = player_form.save(commit=False)
                player.tournament = tournament
                player.save()
            for game_form in game_formset:
                game = game_form.save(commit=False)
                game.tournament = tournament
                game.save()
            return redirect('tournament_details', pk=tournament.pk)
    else:
        form = TournamentForm()
        player_formset = PlayerFormSet(queryset=Player.objects.none(), prefix='players')
        game_formset = GameFormSet(queryset=Game.objects.none(), prefix='games')
    
    return render(request, 'create_tournament.html', {'form': form, 'player_formset': player_formset, 'game_formset': game_formset})

def tournament_details(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    return render(request, 'tournament_details.html', {'tournament': tournament})