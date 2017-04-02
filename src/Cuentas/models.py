from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cuenta(models.Model):
    Numero = models.CharField(max_length=10)
    Titular = models.CharField(max_length=250)
    Monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Titular
