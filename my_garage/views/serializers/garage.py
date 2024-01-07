from .car import CarSerializer
from rest_framework.serializers import CharField, IntegerField, Serializer


class GarageSerializer(Serializer):

    id   = IntegerField(read_only=True)
    name = CharField(max_length=200)
    cars = CarSerializer(source='car_set', many=True)
