import time
import random
from django.core.management.base import BaseCommand
from scores.models import Team, Fixture

class Command(BaseCommand):
    help = 'Load EPL teams and fixtures'

    def handle(self, *args, **kwargs):
        ITERATIONS = 10

        for i in range(ITERATIONS):
            time.sleep(random.randint(1,6))

            # select how many fixtures we're going to update
            update_count = random.randint(1,10)

            # order_by("?") gets random order of rows
            fixtures = Fixture.objects.filter(game_finished=False).order_by("?")

            # get the fixtures we're going to update
            fixtures = fixtures[:update_count]

            self.update_fixtures(fixtures)

            self.is_game_finished(fixtures)

    def update_fixtures(self, fixtures):
        """ Add 1 or 2 goals to each team in the fixture """
        for fixture in fixtures:
            home_goalnow = random.randint(1,2)
            away_goalnow = random.randint(1,2)
            fixture.home_goal += home_goalnow
            fixture.away_goal += away_goalnow

        Fixture.objects.bulk_update(fixtures, ['home_goal', 'away_goal'])

    def is_game_finished(self, fixtures):
        """ With probability 0.3, mark the game as finished """
        for fixture in fixtures:
            # Generate uniform value between 0 and 1
            # If this is < 0.3, then mark game as finished
            P = random.uniform(0,1)
            if P < 0.3:
                fixture.game_finished = True
                fixture.save()