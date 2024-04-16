from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail

from authentication.models import customersModel, customerAddressModel
from master.utils.LO_RANDOM.otp import generate_otp
from master.utils.LO_VALIDATORS.fields import is_valid_email, is_valid_password
from seller.models import productsModel, categoriesModel
from .models import ContactUSModel

import os

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'customer_id' not in request.session:
            messages.warning(request, "You are not logged in yet.")
            return redirect('login_view')
        return view_func(request, *args, **kwargs)
    return wrapper

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        password_ = request.POST['password']
        confirm_password_ = request.POST['c_password']

        if is_valid_email(email_):
            if password_ == confirm_password_:
                is_valid_pwd, msg = is_valid_password(password_)
                if is_valid_pwd:
                    otp_ = generate_otp(6)
                    new_customer = customersModel.objects.create(
                        email = email_,
                        password = password_,
                        otp=otp_
                    )
                    new_customer.save()

                    # send confirmation mail
                    subject = 'Your One-Time Password (OTP) | LOFTY-OUTFITS'
                    message = f"""
                    Dear Customer,

                    Your One-Time Password (OTP) to verify your account is: {otp_}. Please use this code to proceed with the verification process.

                    Thank you.
                    """
                    from_email = os.environ.get('EMAIL_HOST_USER')
                    recipient_list = [f'{email_}']
                    send_mail(subject, message, from_email, recipient_list)

                    context = {
                        'cum_email':email_
                    }
                    messages.warning(request, f"Please check your '{email_}' for the OTP. Enter the received OTP on this confirmation page to verify your email address.")
                    return render(request, 'buyer/otp_verification.html', context)
                else:
                    messages.warning(request, f"{msg}")
                    print(is_valid_password(password_))
                    return redirect('register_view')
            else:
                messages.warning(request, "Password and confirm password does not match.")
                return redirect('register_view')
        else:
            messages.warning(request, "Invalid Email.")
            return redirect('register_view')        
    return render(request, 'buyer/register.html')

def new_customer_otp_verification(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        otp_ = request.POST['otp']
        if otp_.isdigit() and len(otp_) == 6:
            try:
                get_customer = customersModel.objects.get(email=email_)
            except customersModel.DoesNotExist:
                messages.warning(request, "User does not exist.")
                context = {
                    'cum_email': email_
                }
                return render(request, 'buyer/otp_verification.html', context)
            else:
                if get_customer.otp == otp_:
                    get_customer.is_activate = True
                    get_customer.save()
                    messages.success(request, 'Your email has been confirmed. Thank you!')
                    return redirect('login_view')
                else:
                    messages.warning(request, "Invalid OTP.")
                    context = {
                        'cum_email':email_
                    }
                    return render(request, 'buyer/otp_verification.html', context)
        else:
            messages.warning(request, "Invalid OTP input. OTP must be digit[0-9] or only 6 digit(length).")
            context = {
                'cum_email':email_
            }
            return render(request, 'buyer/otp_verification.html', context)


    return render(request, 'buyer/otp_verification.html')

def login_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        password_ = request.POST['password']
        if is_valid_email(email_):
            try:
                get_customer = customersModel.objects.get(email=email_)
            except customersModel.DoesNotExist:
                messages.warning(request, "User does not exist.")
                return redirect('login_view')
            else:
                if get_customer:
                    if get_customer.password == password_:
                        print(get_customer.customer_id, "Added")
                        request.session['customer_id'] = get_customer.customer_id
                        messages.success(request, "Now, you are logged in.")
                        return redirect('index_view')
                    else:
                        messages.warning(request, "Email or Password is not match.")
                        return redirect('login_view')
        else:
            messages.warning(request, "Invalid Email.")
            return redirect('login_view')        

    return render(request, 'buyer/login.html')

def forgot_password_view(request):
    return render(request, 'buyer/forgot.html')

@login_required
def logout(request):
    # request.session.clear()
    del request.session['customer_id']
    messages.success(request, "Now, you are logged out.")
    return redirect('login_view')

def index_view(request):
    return render(request, 'buyer/index.html')

def shopping_view(request):
    categoris = categoriesModel.objects.all()
    products = productsModel.objects.all()
    context = {
        'products':products,
        'categoris':categoris
    }
    return render(request, "buyer/shopping.html", context)

def contact_view(request):
    if request.method == 'POST':
        fname_ = request.POST['first_name']
        lname_ = request.POST['last_name']
        email_ = request.POST['email']
        phone_ = request.POST['phone']
        msg_ = request.POST['message']

        if is_valid_email(email_):
            new_contact = ContactUSModel.objects.create(
                first_name=fname_,
                last_name=lname_,
                email=email_,
                phone=phone_,
                message=msg_
            )
            new_contact.save()
            messages.success(request, "Your request has been submited.")
            return redirect('contact_view')
        else:
            messages.warning(request, "Invalid email")
            return redirect('contact_view')
    return render(request, 'buyer/contact.html')

@login_required
def profile_view(request):
    if 'customer_id' in request.session:
        customer_id_ = request.session['customer_id']
        get_customer = customersModel.objects.get(customer_id=customer_id_)
        get_address = customerAddressModel.objects.get(customer_id=customer_id_)
        print( get_address.street_address, "----")
        context = {
            'get_customer':get_customer,
            'get_address':get_address
        }
        return render(request, 'buyer/profile.html', context)
    else:
        print("Customer ID does not exist in the session")
        return redirect('login_view')

# @login_required
def update_personal_info(request):
    print("here....")
    if request.method == 'POST':
        first_name_ = request.POST['firstname']
        last_name_ = request.POST['lastname']
        mobile_ = request.POST['mobile']

        try:
            get_customer = get_object_or_404(customersModel, customer_id=request.session['customer_id'])
        except customersModel.DoesNotExist:
            messages.warning(request, 'User does not exist.')
            return redirect('profile_view')
        else:
            get_customer.first_name = first_name_
            get_customer.last_name = last_name_
            get_customer.mobile = mobile_
            get_customer.save()
            messages.success(request, 'Profile data updated.')
            return redirect('profile_view')
        
@login_required
def add_address_view(request):
    sa = request.POST['street_address']
    c = request.POST['city']
    p = request.POST['pincode']
    s = request.POST['state']

    try:
        get_customer = get_object_or_404(customersModel, customer_id=request.session['customer_id'])
    except customersModel.DoesNotExist:
        messages.warning(request, 'User does not exist.')
        return redirect('profile_view')
    else:
        new_address = customerAddressModel.objects.create(
            customer_id_id=get_customer.customer_id,
            city=c,
            pincode=p,
            state=s
        )
        new_address.save()
        messages.success(request, 'Address added')
        return redirect('profile_view')


      

