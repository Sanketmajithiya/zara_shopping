from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Book, BookRequest
from .forms import BookForm, BookRequestForm
from django.utils import timezone

# Create your views here.


@login_required
def available_books(request):
    books = Book.objects.filter(available_copies__gt=0)
    return render(request, 'library/available_books.html', {'books': books})

@login_required
def user_books(request):
    book_requests = BookRequest.objects.filter(user=request.user, is_approved=True)
    return render(request, 'library/user_books.html', {'book_requests': book_requests})

@login_required
def request_book(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            book_request = form.save(commit=False)
            book_request.user = request.user
            book_request.save()
            return redirect('user_books')
    else:
        form = BookRequestForm()
    return render(request, 'library/request_book.html', {'form': form})

@login_required
def dashboard(request):
    if not request.user.is_librarian:
        return redirect('available_books')
    return render(request, 'library/dashboard.html')

@login_required
def add_book(request):
    if not request.user.is_librarian:
        return redirect('available_books')
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

@login_required
def manage_requests(request):
    if not request.user.is_librarian:
        return redirect('available_books')
    book_requests = BookRequest.objects.filter(is_approved=False)
    return render(request, 'library/manage_requests.html', {'book_requests': book_requests})

@login_required
def approve_request(request, request_id):
    if not request.user.is_librarian:
        return redirect('available_books')
    book_request = get_object_or_404(BookRequest, id=request_id)
    book_request.is_approved = True
    book_request.renewal_date = timezone.now() + timezone.timedelta(days=14) # 2 weeks
    book_request.book.available_copies -= 1
    book_request.book.save()
    book_request.save()
    return redirect('manage_requests')

@login_required
def revoke_book(request, request_id):
    if not request.user.is_librarian:
        return redirect('available_books')
    book_request = get_object_or_404(BookRequest, id=request_id)
    book_request.book.available_copies += 1
    book_request.book.save()
    book_request.delete()
    return redirect('dashboard')


