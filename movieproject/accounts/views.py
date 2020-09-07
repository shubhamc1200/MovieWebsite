from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm  #form framework provided by django
from django.contrib.auth import login,logout

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
             user=form.save()
             login(request,user)
             return redirect('movies:list')
    else:  #if request.method=='get'
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):  #cant use login as def cuz we are importing login package
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user() # for obtaining user information
            login(request,user) #for logining user also its information(if user info passed as context dict)
                                #if you see admin webpage it will show the user as active
            if 'nextquery' in request.POST: #for create article
                return redirect(request.POST.get('nextquery'))
            else:
                return redirect('movies:list')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('movies:list')
