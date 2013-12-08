from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from polls.models import Poll

def index(request):
    latest_polls = Poll.objects.order_by('-pub_date')[:5]
    output = '<br />'.join(map(lambda poll: poll.question, latest_polls))
    return HttpResponse(output)

def detail(request, poll_id):
    output = ""
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist as e:
        output = 'ERROR: {0}<br />&nbsp&nbsp&nbsp&nbsp{1} - {2}'.format(e, "Poll.id", poll_id)
    else:
        output = "<i>{0})</i> {1}".format(poll_id, poll.question)
    finally:
        return HttpResponse(output)

def results(request, poll_id):
    results = Poll.objects.filter(pk=poll_id)
    output = ''
    if not results:
        output = "The id ({0}) does not exist in the database".format(poll_id)
    else:
        poll = results[0]
        output = "<b>{0}</b><br>\n".format(poll.question)
        output += "<ul>\n"
        for choice in poll.choice_set.filter():
            output += '<li>{0}: {1}</li><br>\n'.format(choice.choice_text, choice.votes)
        output += "</ul>\n"
    return HttpResponse(output)
    
def vote(request, poll_id):
    return HttpResponse("Note yet implemented")
    
# https://docs.djangoproject.com/en/1.6/intro/tutorial03/
# A view is a "type" of Web page in your Django application that generally 
# serves a specific function and has a specific template.
#
# In Django, web pages and other content are delivered by views. Each view is 
# represented by a simple Python function (or method, in the case of class-based views). 
# Django will choose a view by examining the URL that's requested (to be precise, the 
# part of the URL after the domain name).