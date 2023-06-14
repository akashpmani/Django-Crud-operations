from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .forms import registration,CustomLoginForm
from django.contrib.auth.decorators import user_passes_test

from home.models import Student


# Create your views here.

def dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('adminlogin')
        
    
    if request.method == 'POST':
        
            fm = registration(request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['name']
                email = fm.cleaned_data['email']
                password = fm.cleaned_data['password'] 
                
                
                if User.objects.filter(username=username):
                    messages.error(request, "user name already exists")
                    return redirect('dashboard')

                if User.objects.filter(email=email):
                    messages.error(request, "email already exists")
                    return redirect('dashboard')

                myuser = User.objects.create_user(username, email, password)
                myuser.save()

                messages.success(request, "your account has been successfully created")
                return redirect('dashboard')
            
    else:
        fm = registration()
        stud = User.objects.all()
    # user=request.user
    # student=Student.objects.get(user=user)
    # context = {
    #         'student' : student
    #     }
    return render(request,'addupdate.html',{'form' : fm,'users':stud})


def delete_user(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse('dashboard'))

def update_user(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        
        fm = registration(request.POST, instance=pi)
        if fm.is_valid():
            pi.username = fm.cleaned_data['name']
            password = fm.cleaned_data['password']
            pi.set_password(password)
            fm.save()
        

    else :
         pi = User.objects.get(pk=id)
         fm = registration(instance=pi)
    return render(request,'updateuser.html',{'form':fm})



def custom_login(request):
            if request.method == 'POST':
                form = CustomLoginForm(data=request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(request, username=username, password=password)
                    if user is not None and user.is_superuser:
                        request.session['is_admin'] = True
                        login(request, user)
                        return HttpResponseRedirect('/manager')
                    else:
                        return redirect('adminlogin')
                        
            else:
                form = CustomLoginForm()
                return render(request, 'custom_login.html', {'form': form})
        
            # else:
            #     return redirect('adminlogin')
    
def admin_logout(request):
    if  request.session.get('is_admin'):
        request.session.flush()
        logout(request)
    return redirect('/')
    
        
        
    
    
