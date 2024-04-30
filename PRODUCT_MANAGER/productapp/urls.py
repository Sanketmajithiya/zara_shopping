from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # Add URL patterns for adding, updating, and deleting products
    path('search/', views.search, name='search'),
]
