# Register your models here.

from django.contrib import admin
from .models import Category, Product, FeaturedSection

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock_available')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'stock_available')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FeaturedSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('featured_products',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FeaturedSection, FeaturedSectionAdmin)
