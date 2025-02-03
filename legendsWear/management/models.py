from django.db import models

# Create your models here.
class SliderImage(models.Model):
    image = models.ImageField(upload_to="media/")
    caption = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.caption if self.caption else f"Slider Image {self.id}"
    
class Footer(models.Model):
    contact = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=100)
    website_link = models.CharField(max_length=50 )
    address = models.CharField(max_length=200)
    instagram = models.CharField(max_length=90)
    facebook = models.CharField(max_length=90)

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    query = models.TextField()

