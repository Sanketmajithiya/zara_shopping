from django.shortcuts import render, redirect
from .models import auth_admin, Product_name, product_details

# Create your views here.


def is_logged_in(func):
    def wrapper(request, *args,**kwargs):
        if "admin_id" in request.session:
            return func(request, *args,**kwargs)
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
                    return redirect('add_product_name')
                else:
                    print("password wrong")
                    return redirect('admin_login')
    return render(request, "login.html")


@is_logged_in
def add_product_name(request):
    products = Product_name.objects.all()

    if request.method == "POST":
        p_id= request.POST["product_id"]
        p_name= request.POST["product_name"]

        new_product = Product_name.objects.create(p_id=p_id,p_name=p_name)    
        return redirect("add_product_name")

    context = {"products":products}
    return render(request, "add_products.html",context)


def log_out(request):
    try:
        del request.session['admin_id']
    except KeyError:
        print("You were not logged in.")
    else:
        print("You have been successfully logged out.")
    return redirect("admin_login")
   
@is_logged_in
def product_detail(request, p_id):
    product = Product_name.objects.get(p_id=p_id) 
    if request.method == "POST":
        price = request.POST["price"]
        image = request.FILES['image']
        model = request.POST["model"]
        ram = request.POST["ram"]

        new_product = product_details( 
            product_name_id=product.p_id,  
            price=price, 
            image=image, 
            model=model, 
            ram=ram)
        new_product.save()

        return redirect("add_product_name")

    context = {"products": product}
    return render(request, "product_detail.html", context)


