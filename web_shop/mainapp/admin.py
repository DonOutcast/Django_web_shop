from django.contrib import admin
from mainapp.models import ProductCategory, Product

admin.site.register(Product)
admin.site.register(ProductCategory)
