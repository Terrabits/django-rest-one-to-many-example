from .models        import models
from django.contrib import admin


for Model in models:
    admin.site.register(Model)
