from django import forms
from .models import SliderImage, Footer, Contact_Us 

class SliderImageForm(forms.ModelForm):
    class Meta:
        model = SliderImage
        fields = ['SliderImage', 'caption']
        widgets = {
            'SliderImage': forms.ImageField(attrs={'class': 'slider_image'}),
            'caption': forms.TextInput(attrs={'class': 'caption'}),
        }



class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = ['contact']
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
        model = Contact_Us
        fields = {
            'name': forms.TextInput(attrs={'class': 'contact_name'}),
            'contact_no': forms.TextInput(attrs={'class': 'contact_no'}),
            'email': forms.EmailInput(attrs={'class': 'contact_email'}),
            'query': forms.TextArea(attrs={'class': 'query_contact'}),
            }
        
     
  