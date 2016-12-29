from django.conf.urls import url
from Lotes import views

urlpatterns = [
    url(r'^$', views.lotes_list, name='list'),
    url(r'^detail/(?P<id>\d+)/$', views.lotes_detail, name='detail'),
]
