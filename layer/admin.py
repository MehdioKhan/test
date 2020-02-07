from django.contrib import admin
from .models import Figure,Layer,Feature,POI

admin.site.register([Layer,Feature,Figure,POI])