from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



def user_login(request):
    if request.method == 'POST':
       
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
           
            user = authenticate(request,
                username = username,
                password = password
            )
            if user is not None:
                login(request, user)
                request.user.fullname = f"{request.user.first_name} {request.user.last_name}"
                messages.success(request, f"Login successful! {request.user.fullname } Welcome to Dashboard.")
                return redirect('dashboard')
            else:
                messages.error(request,"Username or password is incorrect.")
                return redirect("login")
        except Exception as ex:
            print(str(ex))
            messages.error(request, str(ex))
            return redirect("login")
    return render(request,'users/login.html')




def user_register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password
            )
            if user is not None:
               
                messages.success(request, "Register successful! Welcome to TripBuddy.")
                return redirect('login')
        except Exception as ex:
            print(ex)
            messages.error(request, str(ex))
            return redirect('register')    
    return render(request,'users/register.html')


def user_logout(request):
    logout(request)
    return redirect('login')


