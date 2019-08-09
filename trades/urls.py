from django.conf.urls import url
from trades import views
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^our_clients/', views.our_clients, name='our_clients'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^page/(?P<page_name_slug>[\w\-]+)/$',
        views.show_page, name='show_page'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]