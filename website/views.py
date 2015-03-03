# encoding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    #import ipdb; ipdb.set_trace()
    return render_to_response('website/index.html', {},
                              context_instance=RequestContext(request))