# encoding: utf-8

import urllib2
from dns import resolver
from dns.exception import DNSException

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from itertools import permutations
from random import randint

from .forms import ContactForm
from .models import Type, Resource
import new


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


def dnscheck(request):
    result = False
    url = False
    results_a = []
    results_cname = []
    results_mx = []
    results_ns = []
    if request.method == 'POST':
        url = request.POST.get("url", "").replace("http://", "")
        try:
            opener = urllib2.build_opener()
            result = opener.open('http://' + url)
            opener.close()
            result = True
        except urllib2.HTTPError:
            result = False
        except Exception, e:
            result = False
        #import pdb
        # pdb.set_trace()
        r = resolver.Resolver()
        r.nameservers = ['8.8.8.8', '8.8.4.4']
        r.timeout = 10
        r.lifetime = 10
        try:
            answer = r.query(url, 'A', tcp=True, source='')
            for data in answer:
                results_a.append(data)
        except DNSException:
            results_a = False
        try:
            answer = r.query(url, 'CNAME', tcp=True, source='')
            for data in answer:
                results_cname.append(data)
        except DNSException:
            results_cname = False
        try:
            answer = r.query(url, 'MX', tcp=True, source='')
            for data in answer:
                results_mx.append(data)
        except DNSException:
            results_mx = False
        try:
            answer = r.query(url, 'NS', tcp=True, source='')
            for data in answer:
                results_ns.append(data)
        except DNSException:
            results_ns = False

            '''
            import dns.resolver
            answer = dns.resolver.query("google.com", "A")
            answers = dns.resolver.query('mail.google.com', 'CNAME')
            '''
        ''''''
        if url is not False:
            url = 'http://' + url
    return render_to_response('website/dnscheck.html',
                              {'url': url,
                               'result': result,
                               'results_a': results_a,
                               'results_cname': results_cname,
                               'results_mx': results_mx,
                               'results_ns': results_ns},
                              context_instance=RequestContext(request))


def ochoReinas(request):
    n = 8
    if(n) < 10:
        cols = range(n)
        sol = []
        for vec in permutations(cols):
            if n == len(set(vec[i] + i for i in cols)) and n == len(set(vec[i] - i for i in cols)):
                sol.append(vec)

        board = []
        randSol = sol[randint(0, len(sol) - 1)]
        for b in range(n):
            board.append(list(i for i in range(n)))
        j = 0
        for b in range(n):
            for i in range(n):
                if b % 2 == 0:
                    j = i
                else:
                    j = i + 1
                if j % 2 == 0:
                    cel_class = 'odd'
                else:
                    cel_class = 'even'
                if randSol[b] == i:
                    board[b][i] = {'sol': True, 'class': 'reina'}
                else:
                    board[b][i] = {'sol': False, 'class': cel_class}
            j = j + 1
            #board.append(list(i for i in range(8)))
    return render_to_response('website/8reinas.html',
                              {'board': board,
                               'solutions': randSol},
                              context_instance=RequestContext(request))


def resources(request):
    types = Type.objects.all().order_by('name')
    resources = Resource.objects.all().order_by('title')
    return render_to_response('website/resources.html',
                              {'resources': resources,
                               'types': types},
                              context_instance=RequestContext(request))
