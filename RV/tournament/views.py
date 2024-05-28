from django.shortcuts import render, redirect
from .forms import TournamentForm

def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tournament_list')  # Replace with your success URL
    else:
        form = TournamentForm()
    return render(request, 'create_tournament.html', {'form': form})