from django.shortcuts import render, get_object_or_404
from .models import Product, ProductSubCategory


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Add views for adding, updating, and deleting products

def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = []
    return render(request, 'search_results.html', {'products': products})
