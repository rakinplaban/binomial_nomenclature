from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django import forms
from django.contrib.auth import login as auth_login
from .forms import ContactForm
from .models import ScientificName
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
import json , itertools

def index(request):
    # Get all items and group them by the first letter of `sci_name`
    items = ScientificName.objects.all().order_by('sci_name')
    scientific_name = []
    for letter, group in itertools.groupby(items, lambda item: item.sci_name[0].upper()):
        scientific_name.append((letter, list(group)))  # Convert each group to a list


    content = {
        'scientific_name': scientific_name,
    }

    return render(request, 'nomenclature/index.html', content)



def search(request):
    query = request.GET.get('q', '')
    results = []
    
    if query:
        results = ScientificName.objects.filter(
            Q(sci_name__icontains=query) | Q(real_name__icontains=query)
        )
    
    content = {
        'results': results,
        'query': query,
    }
    return render(request, 'nomenclature/search.html', content)

    

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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to avoid resubmission on refresh
        else:
            messages.error(request, 'There was an error in your form submission.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'nomenclature/success.html')


def about(request):
    return render(request, 'nomenclature/about.html')