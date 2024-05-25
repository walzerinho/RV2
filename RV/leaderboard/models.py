from django.db import models

class Leaderboard(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} - {self.score}"

    class Meta:
        ordering = ['-score']