from django import forms
from .models import Category, Product, FeaturedSection 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name']
        widgets = {
            'category_id' : forms.TextInput(attrs={'class': 'category_id'}), 
            'category_name' : forms.TextInput(attrs={'class': 'category_name'})
        }

class ProductForm(forms.ModelForm):
    class Meta :
        model = Product 
        fields = ['product_id', 'name', 'desc', 'image', 'category']
        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'product_id'}) , 
            'name': forms.TextInput(attrs={'class': 'name'}) , 
            'desc': forms.Textarea(attrs={'class': 'product_desc'}) , 
            'image': forms.ImageField(attrs={'class': 'image'}) , 
            'category': forms.Select(attrs={'class': 'category'})   
        }

class FeaturedSectionForm(forms.ModelForm):
    class Meta:
        model = FeaturedSection
        fields = ['title', 'description', 'featured_products']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}) , 
            'description': forms.TextInput(attrs={'class': 'feature_description'}) , 
            'featured_products': forms.CheckboxSelectMultiple(attrs={'class': 'featured_products'})   
        }

