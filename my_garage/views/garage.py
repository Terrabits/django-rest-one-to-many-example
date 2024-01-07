from ..models     import Garage
from .serializers import GarageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets    import ModelViewSet


class GarageViewSet(ModelViewSet):

    serializer_class   = GarageSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Garage.objects.all().filter(user=user)


    # TODO: custom update() method
    # It should add/remove cars and wheels as necessary to update the current garage...
