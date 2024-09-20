from django.urls import path

from . import views
from django.contrib.auth import login

urlpatterns = [
    path("", views.index, name="index"),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
]