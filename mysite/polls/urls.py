#  To call the view, we need to map it to a URL - and for this we need a URLconf.

from django.conf.urls import patterns, include, url

# mysite/polls/views.py
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
