from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30),
            Activity(user='Captain America', activity_type='Cycling', duration=45),
            Activity(user='Spider-Man', activity_type='Swimming', duration=25),
            Activity(user='Batman', activity_type='Running', duration=40),
            Activity(user='Superman', activity_type='Cycling', duration=50),
            Activity(user='Wonder Woman', activity_type='Swimming', duration=35),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Workouts
        workouts = [
            Workout(name='Hero HIIT', difficulty='Hard', suggested_for='Marvel'),
            Workout(name='Power Yoga', difficulty='Medium', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
