from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import generic
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import login as auth_login
from .forms import CustomLoginForm
from django.views.generic.edit import FormView
from django.contrib import messages
import json

def index(request):
    return render(request, 'nomenclature/index.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return HttpResponseRedirect('index')  # Redirect to a success page.
    else:
        form = CustomLoginForm(request=request)
    return render(request, 'account/login.html', {'form': form})