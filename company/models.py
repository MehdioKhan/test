from django.db import models
from base.models import Model
from django.utils.translation import gettext_lazy as _


class Company(Model):
    name = models.CharField(max_length=70,blank=False,null=False,
                            verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
        ordering = ('name',)

    def __str__(self):
        return self.name
