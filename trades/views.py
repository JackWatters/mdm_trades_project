from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'trades/home.html')


def about(request):
    return HttpResponse("This is the about page. <br/> <a href='/trades/'>Home</a>.")


def contact_us(request):
    return HttpResponse("This is the contact us page.")


def our_clients(request):
    return HttpResponse("This is the our clients page.")











