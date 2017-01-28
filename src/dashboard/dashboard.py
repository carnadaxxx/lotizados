from django.db.models import F, FloatField, Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from Contratos.models import Contrato
from Lotes.models import Manzana, Lote

def HomePage(request):
    if request.user.is_authenticated():
        totalLotes = Lote.objects.count()
        contratos =  Contrato.objects.count()
        porcentage = 100 * float(contratos) / float(totalLotes)
        ultimasVentas = Contrato.objects.order_by('-pk')[:5]
        # suma = Contrato.objects.aggregate(Sum('lote__Costo'))
        # decimal_val = float(suma['lote__Costo__sum'])
        titulo = "HomePage"

        context = {
            # "decimal_val": decimal_val,
            "total" : totalLotes,
            "contratos": contratos,
            "porcentage": porcentage,
            "lastsales": ultimasVentas,
            "titulo": titulo,
        }
        return render(request, "dashboard.html", context)
    else:
        return HttpResponseRedirect('/login/')
