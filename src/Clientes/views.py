from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ClienteForm
from Clientes.models import Cliente

# Create your views here.
def clientes_list(request):
    queryset = Cliente.objects.all()
    context = {
        "titulo": "Lista de Clientes",
        "queryset": queryset,
    }
    return render(request, "clientes/home.html", context)

def cliente_detail(request, id=None):
    queryset = get_object_or_404(Cliente, id=id)
    context = {
        "titulo": "Datos del Cliente",
        "queryset": queryset,
    }
    return render(request, "clientes/detail.html", context)

def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "titulo": "Creacion de Cliente",
        "form": form,
    }
    return render(request, "clientes/form.html", context)

def cliente_update(request, id=None):
    queryset = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = ClienteForm()
    context = {
        "titulo": "Editar informacion del Cliente",
        "queryset": queryset,
        "form": form,
    }
    return render(request, "clientes/form.html", context)

    # queryset = get_object_or_404(Cliente, id=id)
    # form = ClienteForm(request.POST or None, instance=instance)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     instance.save()
    #     return HttpResponseRedirect(instance.get_absolute_url())
    # context = {
    #     "titulo": "Editar del Cliente",
    #     "queryset": queryset,
    #     "form": form,
    # }
    # return render(request, "clientes/form.html", context)
