from django.contrib import admin
from .models import Leaderboard

# Register your models here.
class LeaderboardAdmin(admin.ModelAdmin):
  list_display = ('username', 'score')

admin.site.register(Leaderboard, LeaderboardAdmin)