from django.shortcuts import render, redirect, get_object_or_404
from .forms import TournamentForm, Tournament, Player, PlayerForm, Game, GameForm
# from django.forms import modelformset_factory

def create_tournament(request):

    if request.method == 'POST':
        form = TournamentForm(request.POST)
        player_form = PlayerForm(request.POST)
        game_form = GameForm(request.POST)

        if form.is_valid() and player_form.is_valid() and game_form.is_valid:
            tournament = form.save()
            player = player_form.save()
            game = game_form.save()
            # for i in player_form:
            #     player = i.cleaned_data["name"]
            #     player.tournament = tournament
            #     player.save()

            # for x in game_form:
            #     game = x.save(commit=False)
            #     game.tournament = tournament
            #     game.save()
            return redirect('tournament_details', pk=tournament.pk)
    else:
        form = TournamentForm()
        player_form = PlayerForm()
        game_form = GameForm()
        
    return render(request, 'create_tournament.html', {'form': form})

def tournament_details(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    return render(request, 'tournament_details.html', {'tournament': tournament})