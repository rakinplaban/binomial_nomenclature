from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ContactForm , ScientificNameForm
from .models import ScientificName, Contact
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

    return render(request, 'nomenclature/contact.html', {'form': form})


def success(request):
    return render(request, 'nomenclature/success.html')


def about(request):
    return render(request, 'nomenclature/about.html')



@login_required
def admin_panel(request):
    return redirect('manage_scientific_names')

@login_required
def manage_scientific_names(request):
    scientific_names = ScientificName.objects.all().order_by('sci_name')
    if request.method == 'POST':
        form = ScientificNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_scientific_names')
    else:
        form = ScientificNameForm()
    return render(request, 'admin/manage_scientific_names.html', {'form': form, 'scientific_names': scientific_names})

@login_required
def manage_contacts(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'admin/manage_contacts.html', {'contacts': contacts})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')