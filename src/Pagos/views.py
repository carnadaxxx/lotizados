from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Pago

# Create your views here.
def pagos_list(request):
    if request.user.is_authenticated():
        queryset_list = Pago.objects.all()

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
            "titulo": "Lista de Pagos",
            "queryset": queryset,
        }
        return render(request, "pagos/home.html", context)
    else:
        return HttpResponseRedirect('/login/')
