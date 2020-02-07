from django.db import models
from base.models import Model
from django.utils.translation import gettext_lazy as _


class State(Model):
    name = models.CharField(max_length=25,blank=False,null=False,
                            verbose_name=_("Name"))

    company = models.ForeignKey(to='company.Company',
                                blank=False,null=True,
                                related_name='states',
                                on_delete=models.SET_NULL,
                                verbose_name=_("Company"))

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")
        ordering = ('name','activity_status')

    def __str__(self):
        return self.name

