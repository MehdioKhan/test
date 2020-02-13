from rest_framework import routers
from company import views as company_views
from zone import views as zone_views
from layer import views as layer_views
from driving import views as driving_views
from device import views as device_views


router = routers.DefaultRouter()

# Company
router.register('company',company_views.CompanyViewSet)
# Zone
router.register('state',zone_views.StateViewSet)
# Layer
router.register('layer',layer_views.LayerViewSet)
router.register('figure',layer_views.FigureViewSet)
router.register('feature',layer_views.FeatureViewSet)
router.register('poi',layer_views.POIViewSet)
# Driving
router.register('driver',driving_views.DriverViewSet)
router.register('vehicle',driving_views.VehicleViewSet)
router.register('vehicle_group',driving_views.VehicleGroupViewSet)
# Device
router.register('sensor',device_views.SensorViewSet)
router.register('hardware',device_views.HardwareViewSet)
