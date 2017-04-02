from __future__ import unicode_literals

import math
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


# Create your models here.

class Manzana(models.Model):
    Manzana = models.CharField("Nombre de la Manzana", max_length=150)

    def __unicode__(self):
        return self.Manzana

    def __str__(self):
        return self.Manzana

class Lote(models.Model):
    Manzana = models.ForeignKey(Manzana, on_delete=models.CASCADE)
    Numero = models.PositiveIntegerField()
    Area = models.DecimalField(
        "Area m2",
        max_digits=6,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return str("%s%s" % (self.Manzana, self.Numero))

    def __unicode__(self):
        return str("%s%s" % (self.Manzana, self.Numero))

    def get_absolute_url(self):
        return reverse("lotes:detail", kwargs={"id": self.id})

    def get_costo_metro(self):
        q = settings.COSTO_METRO * float(self.Area)
        return round(q)
