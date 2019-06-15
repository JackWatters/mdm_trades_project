from django.conf.urls import url
from trades import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^our_clients/', views.our_clients, name='our_clients'),
]