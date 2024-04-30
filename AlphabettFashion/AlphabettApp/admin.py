from django.contrib import admin

# Register your models here
from .models import  Product, Watches, HomeAppliances

admin.site.register(Watches)
admin.site.register(Product)
admin.site.register(HomeAppliances)
