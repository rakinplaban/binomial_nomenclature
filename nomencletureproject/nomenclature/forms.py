from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from allauth.account.forms import LoginForm

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['login'].label = 'Email'
        self.fields['login'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['password'].label = 'Password'
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('login', css_class='form-control'),
            Field('password', css_class='form-control'),
            Submit('submit', 'Login', css_class='btn btn-primary')
        )
