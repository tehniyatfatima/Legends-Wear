from django.db import models
import uuid  # To generate unique IDs if needed

# Model 1: Category
class Category(models.Model):
    name = models.CharField(max_length=255)  # Example field

    def __str__(self):
        return self.name

# Model 2: Product
class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated ID
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock_available = models.BooleanField(default=False)  # Default is False

    def __str__(self):
        return self.name

# Model 3: Featured Section
class FeaturedSection(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    featured_products = models.ManyToManyField(Product, related_name='featured_sections')

    def __str__(self):
        return self.title
