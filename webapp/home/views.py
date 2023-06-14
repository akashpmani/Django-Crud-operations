from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import Student

# Create your views here.
# def home(request):
#    if 'username' in request.session:
#         user=request.user
        
#         if Student.objects.get(user=user):
#              student=Student.objects.get(user=user)
#              context = {
#              'student' : student
#              }
#              return render(request,'home.html',context)
#         else:
#             return render(request,'home.html')
            
#    return redirect('signin')

def home(request):
    if 'username' in request.session:
        user = request.user
        
        try:
            student = Student.objects.get(user=user)
            context = {'student': student}
        except Student.DoesNotExist:
            context = {'student': None}
        
        return render(request, 'home.html', context)
    
    return redirect('signin')

    



def signup(request):
    if 'username' in request.session:
        return redirect('home')
    
    if request.method == "POST":
        user_name=request.POST['username']
        email=request.POST['email']
        password1 = request.POST['pass1']  
        password2 = request.POST['pass2']
        
        if User.objects.filter(username=user_name):
            messages.error(request, "user name already exists")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "email already exists")
            return redirect('signup')

        if password1 != password2:
            messages.error(request, "passwords not matching")
            return redirect('signup')

        if not user_name.isalnum():
            messages.error(request, "username can only contain letters and digits")
            return redirect('signup')

        myuser = User.objects.create_user(user_name, email, password1)
        myuser.save()

        messages.success(request, "your account has been successfully created")
        return redirect('signin')
    return render(request,'signup.html')
            

def signin(request):
    if 'username' in request.session:
        return redirect('home')
    if request.method == 'POST':    
        username=request.POST['username']
        password = request.POST['password'] 
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            
            login(request, user)
            request.session['username']=username
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            
        
        
    return render(request,'signin.html')


    
def signout(request):
    if 'username' in request.session:
        request.session.flush()
        logout(request)
    return redirect('signin')
    

    


