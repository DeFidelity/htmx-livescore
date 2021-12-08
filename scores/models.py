from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=222)
    
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=123)
    
    def __str__(self):
        return self.name
    
    
class Fixture(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='fixture',on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_team',on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_team',on_delete=models.CASCADE)
    home_goal = models.PositiveSmallIntegerField(default=0)
    away_goal = models.PositiveSmallIntegerField(default=0)
    game_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"