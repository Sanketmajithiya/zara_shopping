from django.contrib import admin
from .models import Role,Client,Book,BookRequest

# Register your models here.

admin.site.register(Role)
admin.site.register(Client)
admin.site.register(Book)
admin.site.register(BookRequest)