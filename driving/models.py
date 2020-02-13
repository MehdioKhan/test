from django.db import models
from base.models import Model
from django.utils.translation import gettext_lazy as _


class Driver(models.Model):
    first_name = models.CharField(max_length=35,blank=False,null=False,
                                  verbose_name=_("First name"))
    last_name = models.CharField(max_length=50,blank=False,null=False,
                                 verbose_name=_("Last name"))
    nid = models.CharField(max_length=10,blank=True,null=True,
                           verbose_name=_('National code'))
    tel = models.CharField(max_length=10,blank=True,null=True,
                           verbose_name=_("Tel"))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")
        ordering = ('first_name','last_name')

    def full_name(self):
        return "{} {}".format(self.first_name,self.last_name)

    def __str__(self):
        return self.full_name()


class VehicleGroup(Model):

    group_name = models.CharField(max_length=100,
                                  blank=False,null=False,
                                  unique=True,
                                  verbose_name=_("Group name"))

    class Meta:
        verbose_name = _("Vehicle group")
        verbose_name_plural = _("Vehicle groups")
        ordering = ('group_name','activity_status')

    def __str__(self):
        return self.group_name


class Vehicle(Model):
    SERVICE_STATUS = (
        ('ons',_("On service")),
        ('ofs',_("Out of service"))
    )
    title = models.CharField(max_length=70,blank=False,null=False,
                             verbose_name=_("Title"))

    number_plate = models.CharField(max_length=8,blank=False,null=False,
                                    verbose_name=_("Number plate"))
    device = models.ForeignKey(to='device.Hardware',
                               blank=False,null=False,
                               related_name='vehicles',
                               verbose_name=_("Device"),
                               on_delete=models.CASCADE)
    figure = models.ForeignKey(to='layer.Figure',blank=False,null=True,
                               related_name='vehicles',
                               verbose_name=_("Figure"),
                               on_delete=models.SET_NULL)
    vehicle_group = models.ForeignKey(to='driving.VehicleGroup',
                                      blank=False,null=True,
                                      related_name='vehicles',
                                      on_delete=models.SET_NULL,
                                      verbose_name=_("Vehicle group"))
    driver = models.ForeignKey(to='driving.Driver',
                               blank=False,null=True,
                               related_name='vehicles',
                               on_delete=models.SET_NULL,
                               verbose_name=_("Driver"))
    state = models.ForeignKey(to='zone.State',blank=False,null=True,
                              related_name='vehicles',
                              on_delete=models.SET_NULL,
                              verbose_name=_("State"))
    service_status = models.CharField(max_length=3,
                                      blank=False,null=False,
                                      choices=SERVICE_STATUS,
                                      verbose_name=_("Service status"))

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")
        ordering = ('title','driver','state')

    def __str__(self):
        return self.title

