from django import forms
from .models import Contact, ScientificName

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Message',
                'rows': 4
            }),
        }



class ScientificNameForm(forms.ModelForm):
    class Meta:
        model = ScientificName
        fields = ['sci_name', 'real_name']

