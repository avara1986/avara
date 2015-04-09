# encoding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect
from itertools import permutations
from random import randint


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
