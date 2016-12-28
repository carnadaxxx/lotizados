from django.conf.urls import url
from Clientes import views

urlpatterns = [
    url(r'^$', views.clientes_list, name='list'),
    url(r'^detail/(?P<id>\d+)/$', views.cliente_detail, name='detail'),
    url(r'^update/(?P<id>\d+)/$', views.cliente_update, name='update'),
    url(r'^create/$', views.cliente_create, name='create'),
]
