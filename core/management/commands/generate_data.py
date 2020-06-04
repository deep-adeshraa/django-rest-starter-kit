from django.core.management.base import BaseCommand
from core import models as core_models
from django.contrib.auth import models as auth_models
from string import ascii_lowercase, digits
import random
import datetime


class Command(BaseCommand):
    help = "generate random data"

    def handle(self, *args, **kwargs):
        print("generating some users")

        for i in range(10):
            firstname = ''.join([random.choice(
                ascii_lowercase)
                for n in range(5)])

            lastname = ''.join([random.choice(
                ascii_lowercase)
                for n in range(5)])
            password = ''.join([random.choice(
                ascii_lowercase + digits)
                for n in range(8)])
            print(firstname + lastname, password)
            auth_models.User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                email=firstname + '@gmail.com',
                username=firstname + lastname,
                password=password
            )

        places = ['Mumbai,Maharashtra', 'Delhi, Delhi', 'Bengaluru, Karnataka', 'Kolkata, WestBengal',
                  'Chennai, TamilNadu', 'Ahmedabad,Gujarat', 'Jaipur,Rajasthan', 'LucknowUttarPradesh']

        for user in auth_models.User.objects.all():
            core_models.UserInfo.objects.create(
                user=user,
                tz=places[random.randint(0, len(places) - 1)]

            )
            start = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 12),
                                                                 hours=random.choice(range(0, 12)))
            core_models.ActivityPeriods.objects.create(
                user=user,
                start_time=start,
                end_time=start + datetime.timedelta(days=random.randint(0, 12), hours=random.choice(range(0, 12)))
            )
