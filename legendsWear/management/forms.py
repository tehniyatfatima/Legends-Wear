from django import forms
from .models import SliderImage, Footer, ContactUs 

class SliderImageForm(forms.ModelForm):
    class Meta:
        model = SliderImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'slider_image'}),
            'caption': forms.TextInput(attrs={'class': 'caption'}),
        }


class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = ['contact', 'email_address', 'website_link', 'address', 'instagram', 'facebook']  # Include all necessary fields
        widgets = {
            'contact': forms.TextInput(attrs={'class': 'contact'}), 
            'email_address': forms.TextInput(attrs={'class': 'email_address'}), 
            'website_link': forms.TextInput(attrs={'class': 'website_link'}), 
            'address': forms.TextInput(attrs={'class': 'address'}), 
            'instagram': forms.TextInput(attrs={'class': 'instagram'}), 
            'facebook': forms.TextInput(attrs={'class': 'facebook'}), 
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'contact_no', 'email', 'query']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact_name'}),
            'contact_no': forms.TextInput(attrs={'class': 'contact_no'}),
            'email': forms.EmailInput(attrs={'class': 'contact_email'}),
            'query': forms.Textarea(attrs={'class': 'query_contact'}),
        }
