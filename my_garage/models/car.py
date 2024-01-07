from .garage import Garage
from django.contrib.auth.models import User
from django.db.models import CASCADE, CharField, ForeignKey, Model


class Car(Model):

    user   = ForeignKey(User, on_delete=CASCADE)
    name   = CharField(max_length=200)
    garage = ForeignKey(Garage, on_delete=CASCADE)
    # has `wheel_set`
