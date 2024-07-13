from django.urls import path

from . import views
from django.contrib.auth import login

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
    # path("register", views.register, name="register"),

]