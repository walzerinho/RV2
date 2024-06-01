from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    number_of_players = models.IntegerField()
    number_of_games = models.IntegerField()
    FORMAT_CHOICES = [
        ('championship', 'Championship'),
        ('brackets', 'Brackets'),
        ('swiss_round', 'Swiss Round'),
    ]
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    player_names = models.CharField(max_length=100, default="player_name")
    games_names = models.CharField(max_length=100, default="game_name")
    
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    tournament = models.ForeignKey(Tournament, related_name='players', on_delete=models.CASCADE)

class Game(models.Model):
    name = models.CharField(max_length=100)
    number_of_games = models.IntegerField(default=0)
    tournament = models.ForeignKey(Tournament, related_name='games', on_delete=models.CASCADE)