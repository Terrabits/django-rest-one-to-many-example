from django.contrib import admin
from django.urls    import include, path


urlpatterns = [
    path("",       include("my_garage.urls")),
    path("admin/", admin.site.urls),
]
