from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice

# Create your views here.

def index(request):
    latest_polls = Poll.objects.order_by('-pub_date')[:5]
    context = { 'latest_polls': latest_polls }
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id) 
    context = {'poll': poll}
    return render(request, 'polls/detail.html', context)
    
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll details form
        context = {'poll': poll, 'error_message': "You didn't select a choice"}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with
        # POST data. This prevents data from being psoted twice if a user hits the
        # Back button
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {'poll': poll}
    return render(request, 'polls/results.html', context)
        
# https://docs.djangoproject.com/en/1.6/intro/tutorial03/
# A view is a "type" of Web page in your Django application that generally 
# serves a specific function and has a specific template.
#
# In Django, web pages and other content are delivered by views. Each view is 
# represented by a simple Python function (or method, in the case of class-based views). 
# Django will choose a view by examining the URL that's requested (to be precise, the 
# part of the URL after the domain name).