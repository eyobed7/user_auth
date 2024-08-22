
from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


def homepage(request):
   return render(request,"user_app/sui.html")


def is_admin(user):
    return user.role == 'Admin'

def is_librarian(user):
    return user.role == 'Librarian'
def is_member(user):
    return user.role == 'Member'


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('my_login')
    else:
        form = CreateUserForm()
    return render(request, 'user_app/register.html', {'form': form})



def my_login(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid credentials or account inactive")
    return render(request,'user_app/my_login.html',{'loginform':form})
@login_required(login_url="my_login")
def dashboard(request):
    return render(request,'user_app/dashboard.html')


def user_logout(request):
    auth.logout(request)
    return redirect("/")
# Create your views here.
