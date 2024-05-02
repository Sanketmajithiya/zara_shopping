from django.contrib import admin
from .models import Product, ProductSubCategory, auth_admin
# Register your models here.


admin.site.register(Product)
admin.site.register(ProductSubCategory)
admin.site.register(auth_admin)