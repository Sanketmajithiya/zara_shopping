from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductSubCategory,auth_admin


# Create your views here.

def is_logged_in(fx):
    def wrapper(request, *args,**kwargs):
        if "admin_id" in request.session:
            return fx(request, *args,**kwargs)
        else:
            return redirect('admin_login')
    return wrapper


def admin_login(request):
    if request.method == "POST":
        admin_id_ = request.POST["username"]
        password_ = request.POST["password"]
        try:
            check_admin = auth_admin.objects.get(admin_id=admin_id_)
        except:
            print("user wrong")
            return redirect('admin_login')
        else:
            if check_admin:
                if check_admin.password == password_:
                    request.session["admin_id"] = admin_id_
                    return redirect('product_list')
                else:
                    print("password wrong")
                    return redirect('admin_login')
    return render(request, "index.html")
        
@is_logged_in
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@is_logged_in
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

@is_logged_in
def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = []
    return render(request, 'search_result.html')


def log_out(request):
    del request.session['admin_id']
    return redirect("admin_login")