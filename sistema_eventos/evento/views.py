from django.shortcuts import render
from django.views.generic import ListView
from.models import Evento

class EventoListView(ListView):
    model = Evento