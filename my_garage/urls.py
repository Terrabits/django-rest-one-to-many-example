from .              import views
from django.urls    import include, path
from rest_framework import routers


# routes
router = routers.DefaultRouter()
router.register('garages', views.GarageViewSet, basename='garages')


# urls
urlpatterns = [
    path('', include(router.urls)),
]
