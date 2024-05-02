from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('log_out/', views.log_out, name='log_out'),
    path('product_list/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # Add URL patterns for adding, updating, and deleting products
    path('search/', views.search, name='search'),
]
