from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

def HomePage(request):
    if request.user.is_authenticated():
        title = "Sistema de Gestion de Venta de Lotes"
        context = {
            "title": title,
        }
        return render(request, "dashboard.html", context)
    else:
        return HttpResponseRedirect('/login/')
