from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.email, 'test@example.com')

    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        user = User.objects.create_user(username='activityuser', email='activity@example.com', password='pass')
        activity = Activity.objects.create(user=user, type='run', duration=30)
        self.assertEqual(activity.type, 'run')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Leaderboard Team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
