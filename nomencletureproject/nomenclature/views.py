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
import json , itertools

def index(request):
    items  = ScientificName.objects.all().order_by('sci_name')
    # Group the items by the first letter of `sci_name`
    scientific_name = []
    for letter, group in itertools.groupby(items, lambda item: item.sci_name[0].upper()):
        scientific_name.append((letter, list(group)))  # Convert each group to a list

    content = {
        'scientific_name': scientific_name
    }
    return render(request, 'nomenclature/index.html',content)


    

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