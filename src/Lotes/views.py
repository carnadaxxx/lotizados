from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import LoteForm
from Lotes.models import Lote, Manzana

# Create your views here.
def lotes_list(request):
    if request.user.is_authenticated():
        queryset_list = Lote.objects.all()

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

def lotes_update(request, id=None):
    if request.user.is_authenticated():
        instance = get_object_or_404(Lote, id=id)
        if request.method == 'POST':
            form = LoteForm(request.POST or None, instance=instance)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'El lote se edito correctamente')
                return HttpResponseRedirect(instance.get_absolute_url())
            else:
                messages.error(request, 'El cliente No se pudo editar correctamente')
        else:
            form = LoteForm(instance=instance)
        context = {
            "titulo": "Editar informacion del Lote",
            "form": form,
        }
        return render(request, "lotes/update.html", context)
    else:
        return HttpResponseRedirect('/login/')
