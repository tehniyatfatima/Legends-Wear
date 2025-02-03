from django.contrib import admin
from django.utils.html import format_html
from .models import SliderImage, Footer, Contact_Us
from .forms import SliderImageForm, FooterForm, ContactUsForm

class SliderImageAdmin(admin.ModelAdmin):
    form = SliderImageForm
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return "No Image"
    image_tag.short_description = 'Image Preview'
    list_display = ('image_tag', 'caption')  # Use image preview


class FooterAdmin(admin.ModelAdmin):
    form = FooterForm
    list_display = ('contact', 'email_address', 'website_link', 'address', 'instagram', 'facebook')


class ContactUsAdmin(admin.ModelAdmin):
    form = ContactUsForm
    list_display = ('name', 'contact_no', 'email', 'query')

admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Contact_Us, ContactUsAdmin)
