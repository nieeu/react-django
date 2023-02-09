from django.db import models
import string
import random

# Create your models here.
# Define a database model

# Numbers don't lie

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppdercase))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

class Room(models.Model): # a class include these informations
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
