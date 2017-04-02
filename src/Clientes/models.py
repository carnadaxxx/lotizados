from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Cliente(models.Model):
    Nombres = models.CharField(max_length=250)
    ApellidoPaterno = models.CharField(max_length=250)
    ApellidoMaterno = models.CharField(max_length=250)

    def __unicode__(self):
        return u'%s %s' % (self.Nombres, self.ApellidoPaterno)

    def get_contratos(self):
        from Contratos.models import Contrato
        for e in Contrato.objects.filter(titular__id=self.id):
            return e.lote

    def get_absolute_url(self):
        return reverse("clientes:detail", kwargs={"id": self.id})
