from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^orders$', views.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', views.show, name='show'),
    url(r'^order/new/$', views.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', views.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', views.destroy, name='delete'),
]   