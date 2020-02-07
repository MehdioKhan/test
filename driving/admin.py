from django.contrib import admin
from .models import Driver,Vehicle,VehicleGroup

admin.site.register([Driver,Vehicle,VehicleGroup])
