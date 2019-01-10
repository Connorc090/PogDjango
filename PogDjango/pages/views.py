from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html", {})

def champions(request):
    return render(request, "champions.html", {})

def clubs(request):
    return render(request, "clubs.html", {})

def leaderboards(request):
    return render(request, "leaderboards.html", {})
 