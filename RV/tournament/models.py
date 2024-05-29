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
    player_names = models.CharField(max_length=100, default="gpt")
    games_names = models.CharField(max_length=100, default="prout")
    
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    tournament = models.ManyToManyField(Tournament)

class Game(models.Model):
    name = models.CharField(max_length=100)
    number_of_games = models.IntegerField(default=0)