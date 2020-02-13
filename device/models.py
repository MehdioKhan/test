from django.db import models
from base.models import Model
from django.utils.translation import gettext_lazy as _


class Sensor(Model):
    title = models.CharField(max_length=50,blank=False,null=False,
                             verbose_name=_("Title"))

    class Meta:
        verbose_name = _("Sensor")
        verbose_name_plural = _("Sensors")

    def __str__(self):
        return self.title


class Hardware(Model):
    title = models.CharField(max_length=50,blank=False,null=False,
                             verbose_name=_("Title"))
    device_id = models.BigIntegerField(blank=False,null=False,
                                       verbose_name=_("Device ID"))
    os_version = models.CharField(max_length=20,blank=True,null=True,
                                  verbose_name=_("OS Version"))
    ip = models.GenericIPAddressField(blank=False,null=False,
                                      verbose_name=_("IP"))
    sim_card = models.PositiveIntegerField(blank=False,null=False,
                                           verbose_name=_("SIM card Number"))
    sensor_count = models.PositiveIntegerField(blank=False,null=False,
                                               verbose_name=_("Sensor count"))

    class Meta:
        verbose_name = _("Hardware")
        verbose_name_plural = _("Hardware")
        ordering = ('title','device_id')

    def __str__(self):
        return self.title

