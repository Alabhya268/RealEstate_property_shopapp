from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'The username is already taken.')
                return redirect('register')
            
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'The email is already taken.')
                    return redirect('register')
                
                else:
                    user  = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    # Loggin after register
                    # auth.login(request,user)
                    # messages.success(request,"You are now logged in")
                    # return redirect('index')
                    user.save()
                    messages.success(request,"You are now registered and can login")
                    return redirect('login')
                    
        else:
            messages.error(request,'Password did not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        #Login users
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')