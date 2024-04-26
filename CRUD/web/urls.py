from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:student_id>',delete,name='delete'),
    path('edit/<int:student_id>',edit,name='edit')
    
]