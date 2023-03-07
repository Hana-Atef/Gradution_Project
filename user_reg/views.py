from django.shortcuts import render,redirect,HttpResponse
# from .forms import UserForm
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        username = request.POST.get('User_name')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        re_password = request.POST.get('re_pass')
        if password!=re_password:
            return HttpResponse("Your Password and conform password are not same")
        else:
            my_user= User.objects.create_user(username='Hour_Esam',
                                    email='Hoor@beatles.com',
                                    password='123456')
        my_user.save()
        return redirect ('login')
        

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        usernmame = request.POST.get('username')
        password = request.POST.get('your_pass')
        user = authenticate(request,username=usernmame,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is incorrect')
    return render (request,'login.html')
def LogoutPage(request):
    logout(request)
    return redirect('login')


















# def user_list(request):
#   context = {'user_list':User.objects.all()} 
#   return render(request, "user_reg/user_list.html",context)

# def user_form(request , id =0):
#   if request.method == "GET":
#     if id==0:
#       form = UserForm()
#     else:
#       user = User.objects.get(pk=id)
#       form = UserForm(instance=user)
#     return render(request, "user_reg/user_form.html",{'form':form})
#   else:
#     if id == 0:
#       form = UserForm(request.POST)
#     else:
#       user = User.objects.get(pk=id)
#       form = UserForm(request.POST,instance = user)
#     if form.is_valid():
#       form.save()
#     return redirect('/user/list')  

# def user_delete(request,id):
#   user = User.objects.get(pk=id)
#   user.delete()
#   return redirect('/user/list')
