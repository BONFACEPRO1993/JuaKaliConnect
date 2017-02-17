#To use urls function
from django.conf.urls import url
#import from local app login's views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
