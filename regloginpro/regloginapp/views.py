from django.shortcuts import render
from .models import RegistrationData
from .forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse
#
# def home(request):
#     return render(request,'reglogin_home.html')

def registration_view(request):
    if request.method =="POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            fname = request.POST.get('first_name','')
            lname = request.POST.get('last_name','')
            uname = request.POST.get('user_name','')
            pwd = request.POST.get('password','')
            email = request.POST.get('email','')
            number = request.POST.get('number','')

            data = RegistrationData(
                first_name=fname,
                last_name=lname,
                user_name=uname,
                password=pwd,
                email = email,
                number = number
            )
            data.save()
            rform = LoginForm()
            return render(request,'reglogin_login.html',{'rform':rform})
    else:
        rform = RegistrationForm()
        return render(request,'reglogin_reg.html',{'rform':rform})


def login_view(request):
    if request.method =="POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('user_name','')
            password =  request.POST.get('password','')

            un= RegistrationData.objects.filter(user_name=uname)
            pwd = RegistrationData.objects.filter(password=password)

            if not un and pwd:
                return HttpResponse("Invalid Details")
            else:
                return HttpResponse("Valid Details")

    else:
        lform  = LoginForm()
        return render(request,'reglogin_login.html',{'lform':lform})