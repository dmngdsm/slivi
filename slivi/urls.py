from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.get, name='index'),
    url(r'^$', views.get, name='index'),
    url(r'^thanks', views.thanks, name='thanks')

]
