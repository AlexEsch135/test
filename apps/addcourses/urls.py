from django.conf.urls import url
from . import views
def method_to_run(request):
    print "test"
urlpatterns = [
        url(r'^$', views.index),
        url(r'^addcourse$', views.courses),
        url(r'^delete/(?P<id>\d+)$', views.delete),
        url(r'^show/(?P<id>\d+)$', views.show)
        ]
