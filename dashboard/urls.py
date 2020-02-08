from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('status/<tbl_num>',views.Status.as_view(),name='status'),
    path('path/<tbl_num>&<device_id>',views.Path.as_view(),name='path'),
    path('stops/<tbl_num>&<device_id>', views.Stops.as_view(), name='stops'),

]