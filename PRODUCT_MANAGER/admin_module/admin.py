from django.contrib import admin
from .models import auth_admin, Product_name, product_details
# Register your models here.


admin.site.register(auth_admin)
admin.site.register(Product_name)
admin.site.register(product_details)