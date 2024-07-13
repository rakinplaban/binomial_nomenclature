from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import generic
from django import forms
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .forms import CustomLoginForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
# def index(request):
#     return render(request, 'nomenclature/index.html')

class IndexView(generic.ListView):
    template_name = 'nomenclature/index.html'
    def get_queryset(self):
        return None
    
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('first_name'),
            Field('last_name'),
            Field('email'),
            Field('password1'),
            Field('password2'),
            Submit('sign_up', 'Sign Up', css_class='btn-primary')
        )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    

class CustomLoginView(FormView):
    template_name = 'account/login.html'
    form_class = CustomLoginForm

    def get_success_url(self):
        return '/'  # Redirect URL after successful login
    # return reverse('index')  # Reverse URL for the 'index' view

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super().form_valid(form)
            else:
                messages.error(self.request, 'Your account is inactive.')
                return self.form_invalid(form)
            # return super().form_invalid(form)
        else:
            messages.error(self.request, 'Invalid email or password.')
            return self.form_invalid(form)
        
        
    # template_name = 'accounts/login.html'
    # form_class = CustomLoginForm

    # def form_valid(self, form):
    #     user = form.get_user()
    #     if not user.is_active:
    #         messages.error(self.request, 'Your account is inactive.')
    #         return self.form_invalid(form)

    #     login(self.request, user)
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     messages.error(self.request, 'Invalid email or password.')
    #     return super().form_invalid(form)

    # def get_success_url(self):
    #     return HttpResponseRedirect('index')