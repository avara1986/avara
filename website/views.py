# encoding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect


def index(request):
    #import ipdb; ipdb.set_trace()
    return render_to_response('website/index.html', {},
                              context_instance=RequestContext(request))


def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render_to_response('website/contact.html',
                              {'form': form},
                              context_instance=RequestContext(request))
