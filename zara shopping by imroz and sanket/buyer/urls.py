from django.urls import path
from .views import *

urlpatterns = [
    # auth url
    path('register/', register_view, name='register_view'),
    path('otp-verification/', new_customer_otp_verification, name='new_customer_otp_verification'),
    path('login/', login_view, name='login_view'),
    path('forgot_password/', forgot_password_view, name='forgot_password_view'),
    path('logout/', logout, name='logout'),

    # wep page
    path('', index_view, name='index_view'),
    path('shopping/', shopping_view, name='shopping_view'),
    path('contact/', contact_view, name="contact_view"),
    path('profile/', profile_view, name='profile_view'),
    path('profile-update/', update_personal_info, name='update_personal_info'),
    path('add_address_view/', add_address_view, name='add_address_view'),
    path('reset_password_otp_verification/', reset_password_otp_verification, name='reset_password_otp_verification'),
]