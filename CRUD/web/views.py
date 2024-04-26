from django.shortcuts import render,redirect
from .forms import studentform
from .models import student


# Create your views here.
def index(request):
    if request.method == 'POST':
        profile_ = request.FILES['profile']
        first_name_ = request.POST['first_name']
        last_name_ =  request.POST['last_name']
        email_ =  request.POST['email']
        password_ =  request.POST['password']
        print(profile_, first_name_,last_name_,email_, password_)
        # new_student = student.objects.create
       
        new_student = student(profile=profile_ ,first_name= first_name_, last_name=last_name_, email=email_, password=password_)
        new_student.save()
        
    contex = {
        'form':studentform(),
        'students': student.objects.all()
    }
    return render(request, 'index.html', contex)
 
 
def delete(request,student_id):
     print(student_id)
     get_stu = student.objects.get(id=student_id)
     get_stu.delete()
     
     return redirect('index')
 
def edit(request,student_id):
    get_stu = student.objects.get(id=student_id)
    
    if request.method == 'POST':    
       edit_stu = studentform(request.POST, instance=get_stu)
       if edit_stu.is_valid():
           edit_stu.save()
           return redirect('index')
    
    context = {
        'form':studentform(instance=get_stu)
    }
    return render(request,'edit.html',context)

def delete(request,student_id):
    print(student_id)
    get_stu = student.objects.get(id=student_id)
    get_stu.delete()
    return redirect('index')
 
 