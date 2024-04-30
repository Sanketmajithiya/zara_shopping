# from django.shortcuts import render
# from .models import Student, Course, Enrollment

# def home(request):
#     students = Student.objects.all()
#     courses = Course.objects.all()
#     return render(request, 'manage_institute/base.html', {'students': students, 'courses': courses})

# views.py
from django.shortcuts import render
from .models import Student, Teacher, Department

def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    Department = Department.objects.all()
    # books = Book.objects.all()
    return render(request, 'manage_institute/base.html', {'students': students, 'teachers': teachers, 'clubs': Department})

# Add views for managing teachers, clubs, and books as needed































































# from django.shortcuts import render,redirect,get_object_or_404
# from authentication.models import customersModel, customerAddressModel


# # Create your views here.


# import os 

# # def login_required(view_func):
#     def wrapper(request, *args, **kwargs):
#         if 'customer_id' not in request.session:
#             messages.warning(request, "You are not logged in yet.")
#             return redirect('login_view')
#         return view_func(request, *args, **kwargs)
#     return wrapper

# def register_view(request):
#     if request.method == 'POST':
#         email_ = request.POST['email']
#         password_ = request.POST['password']
#         confirm_password_ = request.POST['c_password']
#         try:
#             check_user = customersModel.objects.get(email = email_) 
#         except:
#             check_user = False
            
#         if not check_user:
        
#         #     if is_valid_email(email_):
#         #         if password_ == confirm_password_:
#         #             is_valid_pwd, msg = is_valid_password(password_)
#         #             if is_valid_pwd:
#         #                 otp_ = generate_otp(6)
#         #                 new_customer = customersModel.objects.create(
#         #                     email = email_,
#         #                     password = password_,
#         #                     otp=otp_
#         #                 )
#         #                 new_customer.save()
                        
#         #                                         # send confirmation mail
#         #                 subject = 'Your One-Time Password (OTP) | ZARA-OUTFITS'
#         #                 message = f"""
#         #                 Dear Customer,

#         #                 Your One-Time Password (OTP) to verify your account is: {otp_}. Please use this code to proceed with the verification process.

#         #                 Thank you.
#         #                 """
#         #                 from_email = os.environ.get('EMAIL_HOST_USER')
#         #                 recipient_list = [f'{email_}']
#         #                 send_mail(subject, message, from_email, recipient_list)

#         #                 context = {
#         #                     'cum_email':email_
#         #                 }
#         #                 messages.warning(request, f"Please check your '{email_}' for the OTP. Enter the received OTP on this confirmation page to verify your email address.")
#         #                 return render(request, 'buyer/otp_verification.html', context)
#         #             else:
#         #                 messages.warning(request, f"{msg}")
#         #                 print(is_valid_password(password_))
#         #                 return redirect('register_view')
#         #         else:
#         #             messages.warning(request, "Password and confirm password does not match.")
#         #             return redirect('register_view')
#         #     else:
#         #         messages.warning(request, "Invalid Email.")
#         #         return redirect('register_view') 
            
#         # else:
#             messages.warning(request, "email already exist.")
#             print('email already exist')
#             return redirect('register_view') 
                   
#     return render(request, 'buyer/register.html')

# # def new_customer_otp_verification(request):
#     if request.method == 'POST':
#         email_ = request.POST['email']
#         print(email_)
#         otp_ = request.POST['otp']
#         if otp_.isdigit() and len(otp_) == 6:
#             try:
#                 get_customer = customersModel.objects.get(email=email_)
#             except customersModel.DoesNotExist:
#                 messages.warning(request, "User does not exist.")
#                 context = {
#                     'cum_email': email_
#                 }
#                 return render(request, 'buyer/otp_verification.html', context)
#             else:
#                 if get_customer.otp == otp_:
#                     get_customer.is_activate = True
#                     get_customer.save()
#                     messages.success(request, 'Your email has been confirmed. Thank you!')
#                     return redirect('login_view')
#                 else:
#                     messages.warning(request, "Invalid OTP.")
#                     context = {
#                         'cum_email':email_
#                     }
#                     return render(request, 'buyer/otp_verification.html', context)
#         else:
#             messages.warning(request, "Invalid OTP input. OTP must be digit[0-9] or only 6 digit(length).")
#             context = {
#                 'cum_email':email_
#             }
#             return render(request, 'buyer/otp_verification.html', context)


#     return render(request, 'buyer/otp_verification.html')

# def login_view(request):
#     if request.method == 'POST':
#         email_ = request.POST['email']
#         password_ = request.POST['password']
#         # if is_valid_email(email_):
#             try:
#                 get_customer = customersModel.objects.get(email=email_)
#             except customersModel.DoesNotExist:
#                 messages.warning(request, "User does not exist.")
#                 return redirect('login_view')
#             else:
#                 if get_customer:
#                     if get_customer.password == password_:
#                         print(get_customer.customer_id, "Added")
#                         request.session['customer_id'] = get_customer.customer_id
#                         messages.success(request, "Now, you are logged in.")
#                         return redirect('index_view')
#                     else:
#                         messages.warning(request, "Email or Password is not match.")
#                         return redirect('login_view')
#         # else:
#             # messages.warning(request, "Invalid Email.")
#             return redirect('login_view')        

#     return render(request, 'buyer/login.html')
