from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Cliente(models.Model):
    Nombres = models.CharField(max_length=250)
    ApellidoPaterno = models.CharField(max_length=250)
    ApellidoMaterno = models.CharField(max_length=250)
    FechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return u'%s %s %s' % (self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def get_absolute_url(self):
        return reverse("clientes:detail", kwargs={"id": self.id})
