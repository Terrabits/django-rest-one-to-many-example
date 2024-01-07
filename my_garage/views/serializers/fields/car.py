from ....models import Car
from rest_framework.serializers import PrimaryKeyRelatedField


class CarField(PrimaryKeyRelatedField):

    def get_queryset(self):
        request = self.context['request']
        user    = request.user
        return Car.objects.all().filter(user=user)
