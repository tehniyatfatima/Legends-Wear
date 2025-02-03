from django.shortcuts import render

# Create your views here.
from .models import * 

def slider_view(request):
    slider = SliderImage.objects.all()
    return render(request, 'index.html', {'slider': slider})

def footer_view(request):
    footer = Footer.objects.all()
    return render ()

# Contact_Us