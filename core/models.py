from django.db import models
from django.contrib.auth import models as auth_models
import uuid


# Create your models here.

# class CoreUser(models.AbstractBaseUser):
#     pass

class UserInfo(models.Model):
    """Information about user
        :var
        id = unique id associated to the user
        tz = place associated to the user
        user = one to one relation with user table
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    tz = models.CharField(max_length=200)
    user = models.OneToOneField(auth_models.User, on_delete=models.PROTECT, related_name="info")


class ActivityPeriods(models.Model):
    """
    Activity timings associated to the user
    """
    user = models.ForeignKey(auth_models.User, db_index=True, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
