from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import number_plate_validator

ACTIVE_STATUS = (
        ('a',_("Active")),
        ('d',_("De-active")),
    )


class Driver(models.Model):
    first_name = models.CharField(max_length=35,blank=True,null=True,
                                  verbose_name=_("First name"))
    last_name = models.CharField(max_length=50,blank=True,null=True,
                                 verbose_name=_("Last name"))
    nid = models.CharField(max_length=10,blank=True,null=True,
                           primary_key=True,
                           verbose_name=_('National code'))
    tel = models.PositiveIntegerField(max_length=10,blank=True,
                                      null=True)

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")
        ordering = ('first_name','last_name')

    def full_name(self):
        return "{} {}".format(self.first_name,self.last_name)

    def __str__(self):
        return self.full_name()


class VehicleGroup(models.Model):

    group_name = models.CharField(max_length=100,
                                  blank=False,null=False,
                                  unique=True,
                                  verbose_name=_("Group name"))
    status = models.CharField(max_length=1,choices=ACTIVE_STATUS,
                              verbose_name=_("Status"))

    class Meta:
        verbose_name = _("Vehicle group")
        verbose_name_plural = _("Vehicle groups")
        ordering = ('group_name','status')

    def __str__(self):
        return self.group_name


class Vehicle(models.Model):
    SERVICE_STATUS = (
        ('ons',_("On service")),
        ('ofs',_("Out of service"))
    )
    title = models.CharField(max_length=70,blank=True,null=True,
                             verbose_name=_("Title"))
    activity_status = models.CharField(max_length=1,
                                       choices=ACTIVE_STATUS,
                                       verbose_name=_("Activity status"))
    number_plate = models.CharField(max_length=8,blank=False,null=False,
                                    verbose_name=_("Number plate"),
                                    validators=[number_plate_validator,])
    # device
    # icon
    vehicle_group = models.ForeignKey(to='core.VehicleGroup',
                                      blank=False,null=True,
                                      related_name='vehicles',
                                      on_delete=models.SET_NULL,
                                      verbose_name=_("Vehicle group"))
    driver = models.ForeignKey(to='core.Driver',
                               blank=False,null=True,
                               related_name='vehicles',
                               on_delete=models.SET_NULL,
                               verbose_name=_("Driver"))
    state = models.ForeignKey(to='map.State',blank=False,null=True,
                              related_name='vehicles',
                              on_delete=models.SET_NULL,
                              verbose_name=_("State"))
    service_status = models.CharField(max_length=3,
                                      choices=SERVICE_STATUS,
                                      verbose_name=_("Service status"))
