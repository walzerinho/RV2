from django.contrib import admin
from .models import Tournament

from django.contrib import admin
from .models import Tournament, Player, Game

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1

class GameInline(admin.TabularInline):
    model = Game
    extra = 1

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_players', 'number_of_games', 'format')
    inlines = [PlayerInline, GameInline]

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Player)
admin.site.register(Game)