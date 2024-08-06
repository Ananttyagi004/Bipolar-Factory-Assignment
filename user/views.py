from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


def home(request):
    return render(request, "user/home.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            role = form.cleaned_data.get('role')
            if role == 'ADMIN':
                return redirect("admin-login")
            else:
                return redirect("user-login")
            
    else:
        form = SignUpForm()
    return render(request, "user/signup.html", {"form": form})

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.profile.role == 'ADMIN':
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials or not an admin account")
    return render(request, 'user/login_as_admin.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.profile.role == 'USER':
            login(request, user)
            return redirect('user_dashboard')
        else:
            messages.error(request, "Invalid credentials or not an admin account")
    return render(request, 'user/login_as_user.html')

def custom_logout(request):
    logout(request)
    return redirect("home")

@login_required
def user_dashboard(request):
    return render(request, 'user/user_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'user/admin_dashboard.html')


