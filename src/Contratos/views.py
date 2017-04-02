from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ContratoForm
from .models import Contrato

# Create your views here.
def contratos_list(request):
    if request.user.is_authenticated():
        queryset_list = Contrato.objects.all()

        paginator = Paginator(queryset_list, 10)
        page = request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

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

def contratos_create(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = ContratoForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'El contrato se creo correctamente')
                return HttpResponseRedirect(instance.get_absolute_url())
            else:
                messages.error(request, 'El Contrato No se creo correctamente')
        else:
            form = ContratoForm()
        context = {
            "titulo": "Creacion de Contrato",
            "form": form,
        }
        return render(request, "contratos/create.html", context)
    else:
        return HttpResponseRedirect('/login/')
