from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .form import *
from .models import *
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

class HomePageView(TemplateView):
    template_name = 'index.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class ClassesPageView(TemplateView):
    template_name = 'classes.html'
    
class ContactPageView(TemplateView):
    template_name = 'contact.html'


def RegisterView(request):
    if  request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else :
            messages.error(request, "Ma'lumotlaringizni noto'g'ri kiritdingiz!")
            return redirect('register')
    form = RegisterForm()
    ctx = {
            'form' : form
        }
    
    return render(request, 'register.html',ctx)


def LoginView(request):
    if request.POST:
        username = request.POST["username"]
        password1 = request.POST["password1"]
        user = authenticate(request,username=username, password=password1)
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
                messages.error(request, "Ma'lumotlaringizni noto'g'ri kiritdingiz!")

    form = LoginForm()
    ctx = {
        "form": form,
        
    }
    return render(request, 'login.html',ctx)

def LogoutView(request):
    logout(request)
    return redirect('login')

@login_required()
def ArizaView(request):
    if  request.method == 'POST':
        form = KiderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, "Ma'lumotlaringizni noto'g'ri kiritdingiz!")
    form = KiderForm()
    ctx = {
        "form": form,
        
    }


    return render(request,'ariza.html',ctx)