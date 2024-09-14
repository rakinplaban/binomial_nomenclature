from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import login as auth_login
from .forms import CustomLoginForm
from .models import ScientificName
from django.views.generic.edit import FormView
from django.contrib import messages
from django.db.models import Q
import json

def index(request):
    scientific_name = ScientificName.objects.all()
    content = {
        'scientific_name': scientific_name
    }
    return render(request, 'nomenclature/index.html',content)

# def login_view(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(request.POST, request=request)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return HttpResponseRedirect('index')  # Redirect to a success page.
#     else:
#         form = CustomLoginForm(request=request)
#     return render(request, 'account/login.html', {'form': form})

# def search(request):
#     if request.method == "GET":
#         search = request.GET['q']
#         scientific_name = ScientificName.objects.filter(Q(sci_name__contains=search) | Q(real_name__contains=search))
#         return render(request,"nomenclature/index.html",{
#             "search" : search,
#             'scientific_name': scientific_name
#         })
    

def autocomplete(request):
    if 'term' in request.GET:
        query = request.GET.get('term')
        suggestions = ScientificName.objects.filter(
            Q(sci_name__icontains=query) | Q(real_name__icontains=query)
        )
        results = list(suggestions.values_list('sci_name', flat=True)) + \
                  list(suggestions.values_list('real_name', flat=True))
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)