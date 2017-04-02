from django.conf.urls import url
from Pagos import views

urlpatterns = [
    url(r'^$', views.pagos_list, name='list'),
]
