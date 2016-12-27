from django.http import HttpResponse
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
    context = {
        "form": form,
    }

    return render(request, "clientes/form.html", context)
