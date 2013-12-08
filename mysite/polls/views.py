from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! Time to poll baby.")

# https://docs.djangoproject.com/en/1.6/intro/tutorial03/
# A view is a "type" of Web page in your Django application that generally 
# serves a specific function and has a specific template.
#
# In Django, web pages and other content are delivered by views. Each view is 
# represented by a simple Python function (or method, in the case of class-based views). 
# Django will choose a view by examining the URL that's requested (to be precise, the 
# part of the URL after the domain name).