from __future__ import unicode_literals

from django.db import models
from Contratos.models import Contrato
from Cuentas.models import Cuenta

# Create your models here.
class Pago(models.Model):
    Contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    Cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    NumeroOperacion = models.DecimalField(max_digits=10, decimal_places=0)
    pagado = models.BooleanField()

    def save(self, *args, **kwargs):
        c = Cuenta.objects.get(id=self.Cuenta.id)
        if self.pagado == True:
            c.Monto += self.monto
            c.save()
        super(Pago, self).save(*args, **kwargs)
