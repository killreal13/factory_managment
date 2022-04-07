from django.core.management.base import BaseCommand
from django_seed import Seed
from ...models import *
from ...serializers import json_loader_for_seeder


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('raws_count', nargs='+', type=int)

    def handle(self, *args, **options):
        existing_users = User.objects.all()
        dict_existing_users_data = json_loader_for_seeder(existing_users)
        existing_users = set()
        for user_data in dict_existing_users_data:
            existing_users.add(user_data['fields']['username'])
        seeder_for_users = Seed.seeder()
        seeder_for_workers = Seed.seeder()
        seeder_for_users.add_entity(User, options['raws_count'][0])
        seeder_for_users.execute()
        users = User.objects.exclude(username='kirill')
        dict_user_data = json_loader_for_seeder(users)
        users = set()
        for user_data in dict_user_data:
            users.add(user_data['fields']['username'])
        users.difference_update(existing_users)
        users = list(users)
        for i in range(options['raws_count'][0]):
            user = User.objects.get(username=users[i])
            seeder_for_workers.add_entity(Worker, 1, {'user': user})
        seeder_for_workers.execute()