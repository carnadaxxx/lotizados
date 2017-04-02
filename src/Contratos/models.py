from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from Lotes.models import Lote

from Clientes.models import Cliente
from Lotes.models import Lote

# Create your models here.
class Contrato(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    titular = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    cuotas = models.IntegerField(default = 1 )

    def __str__(self):
        return str("%s %s" % (self.lote, self.titular))

    def get_absolute_url(self):
        return reverse("contratos:detail", kwargs={"id": self.id})

    def save(self, *args, **kwargs):
        self.costo = settings.COSTO_METRO * float(self.lote.Area)
        super(Contrato, self).save(*args, **kwargs)

    class Meta:
        get_latest_by = "order_date"
