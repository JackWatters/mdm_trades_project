from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'trades/home.html')


def about(request):
    return render(request, 'trades/about.html')


def our_clients(request):
    return render(request, 'trades/our_clients.html')


def contact_us(request):
    return render(request, 'trades/contact_us.html')














