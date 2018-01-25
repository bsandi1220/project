import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

from faker import Faker
from app.models import User

fakegen = Faker()

def populate (N=5):
    for entry in range(N):

        fakeName = fakegen.name()
        fakeLast = fakegen.name()

        # Create first and last name
        # fakeName = fakegen.name().split()
        # fake_first_name = fakeName[0]
        # fake_last_name = fakeName[1]


        fakeEmail = fakegen.email()

        userEntry = User.objects.get_or_create(first_name=fakeName, last_name=fakeLast, email=fakeEmail)[0]



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
