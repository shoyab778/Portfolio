from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Full Name',
                'autocomplete': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'your@email.com',
                'autocomplete': 'email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'What is this about?'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Tell me about your project, opportunity, or just say hello...',
                'rows': 6
            }),
        }
