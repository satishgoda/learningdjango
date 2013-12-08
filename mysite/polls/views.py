from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from polls.models import Poll

def index(request):
    latest_polls = Poll.objects.order_by('-pub_date')[:5]
    output = '<br />'.join(map(lambda poll: poll.question, latest_polls))
    return HttpResponse(output)

def detail(request, poll_id):
    
    return HttpResponse("You're looking at poll {0}.".format(poll_id))

def results(request, poll_id):
    return HttpResponse("You are looking at the results of poll {0}.".format(poll_id))

def vote(request, poll_id):
    return HttpResponse("You are voting on poll {0}.".format(poll_id))
    
# https://docs.djangoproject.com/en/1.6/intro/tutorial03/
# A view is a "type" of Web page in your Django application that generally 
# serves a specific function and has a specific template.
#
# In Django, web pages and other content are delivered by views. Each view is 
# represented by a simple Python function (or method, in the case of class-based views). 
# Django will choose a view by examining the URL that's requested (to be precise, the 
# part of the URL after the domain name).