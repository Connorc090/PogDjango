from . import riot
from django.shortcuts import render
from .forms import NameForm
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import urlencode

import json
import requests
    
def index(request):

    form = NameForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']

        base_url = reverse('summoner')
        query_string = urlencode({'name': name})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

    form = NameForm()

    return render(request, './index.html', {'form': form}) 

def summoner(request):
    name = request.GET.get('name')

    solo_duo, flex, tt, formatted_name, level, icon, solo, flexx, twisted = riot.riot_class().call_riot(name)
    
    solo_dict = {}
    flexx_dict = {}
    twisted_dict = {}

    if solo == True:
        solo_dict = {'solo_tier': solo_duo['tier'], 'solo_rank': solo_duo['rank'], 'solo_lp': solo_duo['leaguePoints']}
    if flexx == True:
        flexx_dict = {'flex_tier': flex['tier'], 'flex_rank': flex['rank'], 'flex_lp': flex['leaguePoints']}
    if twisted == True:
        twisted_dict = {'tt_tier': tt['tier'], 'tt_rank': tt['rank'], 'tt_lp': tt['leaguePoints']}

    constants = {'name': formatted_name, 'level': level, 'icon': icon, 'solo': solo, 'flexx': flexx, 'twisted': twisted}

    sent_data = {**solo_dict, **flexx_dict, **twisted_dict, **constants}

    return render(request, "summoner.html", sent_data)

def champions(request):
    return render(request, "champions.html", {})

def clubs(request):
    return render(request, "clubs.html", {})

def leaderboards(request):
    return render(request, "leaderboards.html", {})

 