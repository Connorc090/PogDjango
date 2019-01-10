from . import riot
from django.shortcuts import render
from .forms import NameForm

import json
import requests
    
def index(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  

        riot.call_riot(name)

    form = NameForm()
    
    return render(request, './index.html', {'form': form})

def champions(request):
    return render(request, "champions.html", {})

def clubs(request):
    return render(request, "clubs.html", {})

def leaderboards(request):
    return render(request, "leaderboards.html", {})
 