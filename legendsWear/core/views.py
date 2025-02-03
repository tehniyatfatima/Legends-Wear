from django.shortcuts import render
from .models import Category, Product, FeaturedSection
from .forms import CategoryForm, ProductForm, FeaturedSectionForm

# Create your views here.

## Views to view all Models
# def view_category(request): 
#     category = Category.objects.all()
#     return render(request, 'category.html', {'category': category})

# def view_product(request):
#     product = Product.objects.all()
#     return render(request, 'product.html', {'product': product})

# def view_FeaturedSection(request):
#     featured_section = FeaturedSection.objects.all()
#     return render(request, 'featured_section.html', {'featured_section': featured_section})


# =======================================================================================================================================================================
# =======================================================================================================================================================================


# One View to Display Home Page :  
# def home_page(request):  
#     category = Category.objects.all()  
#     product = Product.objects.all()  
#     featured_section = FeaturedSection.objects.all()  
#     return render(request, 'index.html', {'category': category, 'product': product, 'featured_section': featured_section})  
from django.shortcuts import render
from .models import Category, Product

def store_home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {'categories': categories, 'products': products})


## Views to add/edit all Models
# 1. This can be add and edit through admin because the website is only a landing page mean one page

