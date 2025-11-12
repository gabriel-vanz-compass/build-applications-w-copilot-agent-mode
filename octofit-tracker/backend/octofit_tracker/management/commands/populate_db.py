from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com'),
            User.objects.create_user(username='captainamerica', email='captainamerica@marvel.com'),
            User.objects.create_user(username='batman', email='batman@dc.com'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com'),
        ]

        # Create activities
        Activity.objects.create(name='Run', user_email='ironman@marvel.com', team='Marvel')
        Activity.objects.create(name='Swim', user_email='captainamerica@marvel.com', team='Marvel')
        Activity.objects.create(name='Fly', user_email='batman@dc.com', team='DC')
        Activity.objects.create(name='Lift', user_email='wonderwoman@dc.com', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=200)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Lift heavy objects')
        Workout.objects.create(name='Flight Training', description='Practice flying')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
