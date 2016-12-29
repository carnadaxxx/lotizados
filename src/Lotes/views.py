from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from Lotes.models import Lote, Manzana

# Create your views here.
def lotes_list(request):
    if request.user.is_authenticated():
        queryset = Lote.objects.all()
        context = {
            "titulo": "Lista de Lotes",
            "queryset": queryset,
        }
        return render(request, "lotes/home.html", context)
    else:
        return HttpResponseRedirect('/login/')

def lotes_detail(request, id=None):
    if request.user.is_authenticated():
        queryset = get_object_or_404(Lote, id=id)
        context = {
            "titulo": "Datos del Lote",
            "queryset": queryset,
        }
        return render(request, "lotes/detail.html", context)
    else:
        return HttpResponseRedirect('/login/')
