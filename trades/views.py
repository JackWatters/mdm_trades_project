from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the home page. <br/> <a href='/trades/about/'>About</a>.")


def about(request):
    return HttpResponse("This is the about page. <br/> <a href='/trades/'>Home</a>.")


def contact_us(request):
    return HttpResponse("This is the contact us page.")


def our_clients(request):
    return HttpResponse("This is the our clients page.")











