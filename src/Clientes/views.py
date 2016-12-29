from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ClienteForm
from Clientes.models import Cliente

# Create your views here.
def clientes_list(request):
    if request.user.is_authenticated():
        queryset = Cliente.objects.all()
        context = {
            "titulo": "Lista de Clientes",
            "queryset": queryset,
        }
        return render(request, "clientes/home.html", context)
    else:
        return HttpResponseRedirect('/login/')

def cliente_detail(request, id=None):
    if request.user.is_authenticated():
        queryset = get_object_or_404(Cliente, id=id)
        context = {
            "titulo": "Datos del Cliente",
            "queryset": queryset,
        }
        return render(request, "clientes/detail.html", context)
    else:
        return HttpResponseRedirect('/login/')

def cliente_create(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = ClienteForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'El cliente se creo correctamente')
                return HttpResponseRedirect(instance.get_absolute_url())
            else:
                messages.error(request, 'El cliente No se creo correctamente')
        else:
            form = ClienteForm()
        context = {
            "titulo": "Creacion de Cliente",
            "form": form,
        }
        return render(request, "clientes/create.html", context)
    else:
        return HttpResponseRedirect('/login/')


def cliente_update(request, id=None):
    if request.user.is_authenticated():
        instance = get_object_or_404(Cliente, id=id)
        if request.method == 'POST':
            form = ClienteForm(request.POST or None, instance=instance)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'El cliente se edito correctamente')
                return HttpResponseRedirect(instance.get_absolute_url())
            else:
                messages.error(request, 'El cliente No se pudo editar correctamente')
        else:
            form = ClienteForm(instance=instance)
        context = {
            "titulo": "Editar informacion del Cliente",
            "form": form,
        }
        return render(request, "clientes/update.html", context)
    else:
        return HttpResponseRedirect('/login/')           
