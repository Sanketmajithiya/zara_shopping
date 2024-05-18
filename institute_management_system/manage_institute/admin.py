from django.contrib import admin
from .models import  Student,Teacher,clubs,books

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(clubs)
admin.site.register(books)