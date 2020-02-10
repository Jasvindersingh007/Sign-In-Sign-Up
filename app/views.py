from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import emp
# Create your views here.

def empdata(request):
    if request.method== 'POST':
        name = request.POST['ename']
        salary = request.POST['esalary']
        date_of_joining = request.POST['edoj']
        
        emp_obj = emp(name=name,salary=salary,doj=date_of_joining)
        emp_obj.save();
        messages.info(request, 'User created')
        return redirect('/')
        
    else:
        return HttpResponse(request, 'Go back & enter some data plz..')

def userlogin(request):
    if request.method== 'POST':
        username = request.POST['uname']
        password = request.POST['upwd']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'welcome')
            return redirect('/home')

        else:
            messages.info(request, 'invalid ')
            return HttpResponse('invalide')

    else:
        return render(request, 'login')

def logout(request):
     auth.logout(request)
     return redirect('/')
 
def processed(request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['pwd']
        password2 = request.POST['cpwd']
        
        if password1==password2:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=name,email=email,password=password1)
                user.save();
                messages.info(request, 'User created')
                return redirect('login')

        else:
            messages.info(request, 'Password Not Matching')
        return redirect('register')
        
            
    else:
        return render(request, 'register')
        
def index(request):
    es = emp.objects.all()
    return render(request, 'page/index.html', {'es': es})

def register(request):
    return render(request, 'page/register.html')

def login(request):
    return render(request, 'page/login.html')