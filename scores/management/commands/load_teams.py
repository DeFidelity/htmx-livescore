from django.core.management.base import BaseCommand
from scores.models import Team, Tournament, Fixture


TEAMS = [
    'Liverpool','Barcelona','Ajax','Manchester City', 'Real Madrid','Napoli','Juventus','Liecester','Chelsea',
    'PSG','Atletico Madrid','AC Milan','Bayern Munich','Arsenal','Villareal','Young Boys','Kano Pillars','Al-Hillah',
    'Real Betis','Everton','Brentford','Milan','Bayern Leverkusean','Bilbao','Lion','Wattford','Shooting Star','Norwich'
]


class Command(BaseCommand):
    help = 'Load Champions League teams and fixtures'

    def handle(self, *args, **kwargs):
        # add tournament 
        tournament = Tournament.objects.get_or_create(name="Champions League")[0]
        
        #add team 
        if Team.objects.count() == 0:
            team_objs = [Team(name=team_name) for team_name in TEAMS]
            teams = Team.objects.bulk_create(team_objs)
            teams.objects.save()
        else:
            teams = Team.objects.all()
            
        # create fixture set with two following teams
        fixtures = []
        for i in range(0,len(teams), 2):
           fixtures.append(
               Fixture(home_team=teams[i], away_team=teams[i+1], tournament=tournament)
                                                      
           )
        if Fixture.objects.count() == 0:
            fixtures = Fixture.objects.bulk_create(fixtures)