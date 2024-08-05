from django.shortcuts import render,redirect
from .models import Book,BookRequest,Client

# Create your views here.

def login(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        password_ = request.POST['password']
        client = Client.objects.get(email=email_)
        if client.password == password_:
            response = redirect('dashboardView')
            response.set_cookie("role",client.role)
            response.set_cookie("firstname",client.firstname)
            return response
            
    return render(request,"library/login.html")

def logout(request):
    return redirect('login')

def dashboardView(request):
    books = Book.objects.all()
    context = {
        "books" : books,
    }
    return render(request, 'library/dashboard.html',context)

def assignBookView(request):
    books = {}
    object = request.COOKIES.get("role")
    if object == "librarian":
        books = BookRequest.objects.all()
    else:
        books = BookRequest.objects.filter(client__firstname=request.COOKIES.get("firstname"))
    context = {
        "books" : books
    }
    return render(request, 'library/assignbook.html',context)

def requestBookView(request):
    books = BookRequest.objects.all()
    context = {
        "books" : books
    }
    return render(request, 'library/requestbook.html',context)

def approvedRequest(request,name,book_title):
    client = BookRequest.objects.filter(client__firstname=name,book__title=book_title).first()
    if request.method=="POST":
        approve_ = request.POST.get("approve")
        if approve_ == "on":
            client.approved = True
            client.save()
            return redirect("assignBookView")
        

def Editpage(request,pk):
    get_data = Book.objects.get(id=pk)
    return render(request,"edit.html", {'key2':get_data})
    
       
def update_view(request,pk):
    book = Book.objects.get(id=pk)
    book.title = request.POST["title"]
    book.author = request.POST["author"]
    book.published_date = request.POST["published_date"]
    book.is_in_stock = request.POST["is_in_stock"]
    book.save()
    
    return redirect('dashboardView')


def DeleteData(request,pk):
    ddata = Book.objects.get(id=pk)
    ddata.delete()
    return redirect('dashboardView')






