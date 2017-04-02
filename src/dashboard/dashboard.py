from django.db.models import F, FloatField, Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from Contratos.models import Contrato
from Lotes.models import Manzana, Lote
from Cuentas.models import Cuenta

def HomePage(request):
    if request.user.is_authenticated():
        totalLotes = Lote.objects.count()
        contratos =  Contrato.objects.count()
        cuentas = Cuenta.objects.all()
        # porcentage = 100 * float(contratos) / float(totalLotes)
        ultimasVentas = Contrato.objects.order_by('-pk')[:4]
        # suma = Contrato.objects.aggregate(Sum('lote__Costo'))
        # decimal_val = float(suma['lote__Costo__sum'])
        titulo = "HomePage"

        context = {
            # "decimal_val": decimal_val,
            "total" : totalLotes,
            "cuentas": cuentas,
            "contratos": contratos,
            # "porcentage": porcentage,
            "lastsales": ultimasVentas,
            "titulo": titulo,
        }
        return render(request, "dashboard.html", context)
    else:
        return HttpResponseRedirect('/login/')
