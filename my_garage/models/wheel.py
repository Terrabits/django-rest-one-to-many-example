from .car import Car
from django.contrib.auth.models import User
from django.db.models import CASCADE, CharField, ForeignKey, Model


class Wheel(Model):

    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=200)
    car  = ForeignKey(Car, on_delete=CASCADE)
