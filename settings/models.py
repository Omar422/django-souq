from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Brand(models.Model):

    brdname = models.CharField(max_length=40, verbose_name=_('Name'))
    brddesc = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.brdname


class Variant(models.Model):
    
    varname = models.CharField(max_length=40, verbose_name=_('Name'))
    vardesc = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.varname
