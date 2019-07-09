import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mdm_trades_project.settings')
import django
django.setup()
from trades.models import Category, Page


def populate():

    client_pages = [
        {"title": "cala homes",
         "url": "https://www.cala.co.uk",
         "description": ""},
        {"title": "Persimmon homes",
         "url": "https://www.persimmonhomes.com",
         "description": ""},
        {"title": "Avant homes",
         "url": "https://www.avanthomes.co.uk",
         "description": ""}]

    cats = {"Clients": {"pages": client_pages}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Trades population script...")
    populate()