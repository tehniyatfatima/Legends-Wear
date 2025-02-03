from django import forms
from .models import Category, Product, FeaturedSection

# Form for Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'})
        }

# Form for Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'stock_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter product description', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'stock_available': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

# Form for Featured Section
class FeaturedSectionForm(forms.ModelForm):
    class Meta:
        model = FeaturedSection
        fields = ['title', 'description', 'featured_products']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter section title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter section description', 'rows': 4}),
            'featured_products': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
