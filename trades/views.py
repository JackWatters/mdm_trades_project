from django.shortcuts import render
from django.http import HttpResponse
from trades.models import Category, Page


def home(request):
    return render(request, 'trades/home.html')


def about(request):
    return render(request, 'trades/about.html')


def our_clients(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'trades/our_clients.html', context_dict)


def contact_us(request):
    return render(request, 'trades/contact_us.html')


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'trades/category.html', context_dict)


def show_page(request, page_name_slug):
    context_dict = {}
    try:
        page = Page.objects.get(slug=page_name_slug)
        description = Page.objects.filter(description=page.description)
        url = Page.objects.filter(url=page.url)
        context_dict['page'] = page
        context_dict['description'] = description
        context_dict['url'] = url
    except Category.DoesNotExist:
        context_dict['page'] = None
        context_dict['description'] = None
        context_dict['url'] = None
    return render(request, 'trades/client.html', context_dict)














