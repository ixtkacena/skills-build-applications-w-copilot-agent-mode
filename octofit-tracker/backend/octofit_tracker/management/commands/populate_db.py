
from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(host='localhost', port=27017)
        db = client['octofit_db']

        # Clear existing collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email for users
        db.users.create_index({'email': 1}, unique=True)

        # Sample data
        marvel_team = {
            'name': 'Marvel',
            'members': ['Iron Man', 'Captain America', 'Thor', 'Black Widow']
        }
        dc_team = {
            'name': 'DC',
            'members': ['Superman', 'Batman', 'Wonder Woman', 'Flash']
        }
        db.teams.insert_many([marvel_team, dc_team])

        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'team': 'Marvel'},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team': 'Marvel'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Flash', 'email': 'flash@dc.com', 'team': 'DC'},
        ]
        db.users.insert_many(users)

        activities = [
            {'user': 'Iron Man', 'activity': 'Running', 'duration': 30},
            {'user': 'Superman', 'activity': 'Flying', 'duration': 60},
            {'user': 'Batman', 'activity': 'Martial Arts', 'duration': 45},
            {'user': 'Wonder Woman', 'activity': 'Weightlifting', 'duration': 50},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {'team': 'Marvel', 'points': 120},
            {'team': 'DC', 'points': 110},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {'user': 'Thor', 'workout': 'Hammer Lifts', 'reps': 100},
            {'user': 'Flash', 'workout': 'Sprints', 'reps': 200},
        ]
        db.workouts.insert_many(workouts)

        print('octofit_db database populated with test data.')
