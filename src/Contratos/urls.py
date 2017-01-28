from django.conf.urls import url
from Contratos import views

urlpatterns = [
    url(r'^$', views.contratos_list, name='list'),
    url(r'^detail/(?P<id>\d+)/$', views.contratos_detail, name='detail'),
    url(r'^create/$', views.contratos_create, name='create'),
]
