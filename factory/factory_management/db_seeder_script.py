from django_seed import Seed
from .models import *


seeder = Seed.seeder()
seeder.add_entity(Worker, 5)
seeder.excecute()