from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Poll, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_polls'
    
    def get_queryset(self):
        """Return the last five published polls"""
        return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = "polls/detail.html"
    
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

class ResultsView(generic.DetailView):
    model = Poll
    template_name = "polls/results.html"

# https://docs.djangoproject.com/en/1.6/intro/tutorial03/
# A view is a "type" of Web page in your Django application that generally 
# serves a specific function and has a specific template.
#
# In Django, web pages and other content are delivered by views. Each view is 
# represented by a simple Python function (or method, in the case of class-based views). 
# Django will choose a view by examining the URL that's requested (to be precise, the 
# part of the URL after the domain name).