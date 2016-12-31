from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from Lotes.models import Lote
from Clientes.models import Cliente

# Create your models here.
class Contrato(models.Model):
    lote = models.ForeignKey(
        Lote,
        on_delete=models.CASCADE,
    )
    titular = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    creado = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )

    def __str__(self):
        return str("%s %s" % (self.lote, self.titular))

    def get_absolute_url(self):
        return reverse("contratos:detail", kwargs={"id": self.id})


    class Meta:
        get_latest_by = "order_date"
