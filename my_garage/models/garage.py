from django.contrib.auth.models import User
from django.db.models import CASCADE, CharField, ForeignKey, Model


class Garage(Model):

    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=200)
    # has `car_set`
