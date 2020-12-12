from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from . models import Ticket
import random
# Create your views here.
def buy_ticket(request):
    context = {'tickets': Ticket.objects.all()}
    return render(request, 'ticket/home.html', context)
