from django.shortcuts import render,redirect
from django.contrib import messages
from .models import EB_Staff

def layout(request):
    return render(request, 'layout.html')

def index(request):

    return render(request, 'index.html')

def employee_login(request):
    if request.method == 'POST':
       try:
           Officedetails = EB_Staff.objects.get(username=request.POST['username'],password=request.POST['password'])
           print("username=",Officedetails)
           request.session['username']= Officedetails.username
           return redirect('/')
       except EB_Staff.DoesNotExist as e:
           messages.success(request,'Username / Password Invalid..!')
    return render(request, 'employee_login.html')

def EB_logout(request):
    try:
        del request.session['username']
    except:
        return render(request, 'employee_login.html')
    return render(request, 'employee_login.html')

def owndata(request):
        return render(request, 'owndata.html')


def custdel(request):
    return render(request, 'custdel.html')


def owndel(request):
        return render(request, 'owndel.html')

