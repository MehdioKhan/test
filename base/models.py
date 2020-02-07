from django.db import models
from django.utils.translation import gettext_lazy as _

ACTIVE_STATUS = (
        ('a',_("Active")),
        ('d',_("De-active")),
)


class Model(models.Model):
    activity_status = models.CharField(max_length=1,
                                       blank=False,null=False,
                                       choices=ACTIVE_STATUS,
                                       verbose_name=_("Activity status"))

    class Meta:
        abstract = True

