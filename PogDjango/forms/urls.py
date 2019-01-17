from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('champions/', views.champions, name='champions'),
    path('clubs/', views.clubs, name='clubs'),
    path('leaderboards/', views.leaderboards, name='leaderboards'),
    path('summoner/', views.summoner, name='summoner')
]
