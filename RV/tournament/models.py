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
    
    def __str__(self):
        return self.name
