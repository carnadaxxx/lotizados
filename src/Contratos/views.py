from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Contrato

# Create your views here.
def contratos_list(request):
    if request.user.is_authenticated():
        queryset = Contrato.objects.all()
        context = {
            "titulo": "Lista de Contratos",
            "queryset": queryset,
        }
        return render(request, "contratos/home.html", context)
    else:
        return HttpResponseRedirect('/login/')

def contratos_detail(request, id=None):
    if request.user.is_authenticated():
        queryset = get_object_or_404(Contrato, id=id)
        context = {
            "titulo": "Datos del Contrato",
            "queryset": queryset,
        }
        return render(request, "contratos/detail.html", context)
    else:
        return HttpResponseRedirect('/login/')
