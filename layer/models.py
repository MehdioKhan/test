from django.db import models
from base.models import Model
from django.utils.translation import gettext_lazy as _


class Feature(Model):
    title = models.CharField(max_length=50,blank=False,null=False,
                             verbose_name=_("Title"))

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
        ordering = ('title',)

    def __str__(self):
        return self.title


class Layer(Model):
    title = models.CharField(max_length=50,blank=False,null=False,
                             verbose_name=_("Layer"))
    features = models.ManyToManyField(to='layer.Feature',blank=True,
                                      related_name='layer_features',
                                      verbose_name=_("Features"))

    class Meta:
        verbose_name = _("Layer")
        verbose_name_plural = _("Layers")
        ordering = ('title',)

    def __str__(self):
        return self.title


class Figure(Model):

    MARKERS = (
        ('cr',_("Circle")),
        ('sq',_("Square")),
        ('st',_("Star")),
        ('pg',_("Polygon")),
    )
    title = models.CharField(max_length=50,blank=False,null=False,
                             verbose_name=_("Title"))
    icon = models.CharField(max_length=30,blank=False,null=False,
                            verbose_name=_("Icon"))
    color = models.CharField(max_length=6,blank=False,null=False,
                             verbose_name=_("Color"))
    marker_shape = models.CharField(max_length=2,
                                    blank=False,null=False,
                                    choices=MARKERS)

    class Meta:
        verbose_name = _("Figure")
        verbose_name_plural = _("Figures")
        ordering = ('title','activity_status')

    def __str__(self):
        return self.title


class POI(models.Model):
    title = models.CharField(max_length=50,blank=False,null=False,
                             verbose_name=_("Title"))
    figure = models.ForeignKey(to='layer.Figure',blank=False,null=True,
                               related_name='pois',
                               verbose_name=_("Figure"),
                               on_delete=models.SET_NULL)
    layer = models.ForeignKey(to='layer.Layer',blank=False,null=True,
                              related_name='pois',
                              verbose_name=_("Layer"),
                              on_delete=models.SET_NULL)
    longitude = models.DecimalField(max_digits=16,decimal_places=14)
    latitude = models.DecimalField(max_digits=16,decimal_places=14)

    class Meta:
        verbose_name = _("Point of interest")
        verbose_name_plural = _("Points of interest")
        ordering = ('title',)

    def __str__(self):
        return self.title


