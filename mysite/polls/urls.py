#  To call the view, we need to map it to a URL - and for this we need a URLconf.

from django.conf.urls import patterns, include, url

# mysite/polls/views.py
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/detail/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
)
