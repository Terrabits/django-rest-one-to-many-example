# from ...models import Garage
from .fields   import GarageField
from .wheel    import WheelSerializer
from rest_framework.serializers import CharField, Serializer


class CarSerializer(Serializer):

    name   = CharField(max_length=200)
    garage = GarageField()
    wheels = WheelSerializer(source='wheel_set', many=True)
