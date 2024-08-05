from django.urls import path, include
from .views import *

urlpatterns = [
    path('', available_books, name='available_books'),
    path('my_books/', user_books, name='user_books'),
    path('request_book/', request_book, name='request_book'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_book/', add_book, name='add_book'),
    path('manage_requests/', manage_requests, name='manage_requests'),
    path('approve_request/<int:request_id>/', approve_request, name='approve_request'),
    path('revoke_book/<int:request_id>/', revoke_book, name='revoke_book'),
]