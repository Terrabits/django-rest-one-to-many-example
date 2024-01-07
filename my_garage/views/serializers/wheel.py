from .fields import CarField
from rest_framework.serializers import CharField, Serializer


class WheelSerializer(Serializer):

    name = CharField(max_length=200)
    car  = CarField()
