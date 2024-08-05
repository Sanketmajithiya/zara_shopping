from django import forms
from .models import Book, BookRequest

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'total_copies']

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ['book']
