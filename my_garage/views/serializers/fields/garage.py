from ....models import Garage
from rest_framework.serializers import PrimaryKeyRelatedField


class GarageField(PrimaryKeyRelatedField):

    def get_queryset(self):
        request = self.context['request']
        user    = request.user
        return Garage.objects.all().filter(user=user)
