from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth import login

urlpatterns = [
    path("", views.index, name="index"),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    # For admin
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/scientific-names/', views.manage_scientific_names, name='manage_scientific_names'),
    path('admin-panel/contacts/', views.manage_contacts, name='manage_contacts'),
    path('admin-panel/login/', LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]