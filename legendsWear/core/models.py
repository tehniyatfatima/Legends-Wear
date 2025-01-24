from django.db import models

# Create your models here.
# Model 1 Categories
# Categories ID
# Categories Name
class Category(models.Model):
    category_id = models.CharField(max_length=10, unique=True, editable=False)
    category_name = models.CharField(max_length=50)

# Model 2 Products
# Product ID   
# Product Name 
# Product Desc 
# Product Image
# Product associated with Category (show all drop down in categories)
# Stock Availability (Boolean field)
class Product(models.Model):
    id = models.CharField()
    name = models.CharField()
    desc = models.TextField()
    image = models.ImageField(upload_to="products/")
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    
# Model 3  Featured section
# Here all product will listed, user have to check desire product which want to show in featured section
class FeaturedSection(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    # Many-to-Many relationship to associate multiple products with this featured section
    featured_products = models.ManyToManyField(Product, related_name='featured_sections')
    
    def __str__(self):
        return self.title

