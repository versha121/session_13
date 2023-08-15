from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Home
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.

def UserRegister(request):
    direct_to_home =0
    if request.method =="POST":
        email=request.POST.get("email","")
        fname=request.POST.get("fname","")
        name=request.POST.get("name","")
        Class=request.POST.get("Class","")
        age=request.POST.get("age","")
        gender=request.POST.get("gender","")
        password=request.POST.get("password","")

        print("name is",name)
        print("fname is",fname)
        print("email is",email)

        user = User()
        user.first_name= name
        user.username = email
        # user.email = email
        user.set_password(password)
        print(user)
        # if User.objects.filter(username = user.username).first():
        #     messages.error(request, "This username is already taken")
        #     return redirect('/home/')
        # else:
        user.save()
        
        

        # direct_to_home = 1
        # if direct_to_home == 1:
        #     return redirect("/home/")
        return render (request,'UserRegister.html',{"msg":"User Registered Successfully"})
    return render (request,'UserRegister.html')


def UserLogin(request):
    print("In User Login ")
    if request.method=="POST":
        print("In If line 53")
        username1=request.POST.get("Username","")
        password =request.POST.get("password","")

        print("username",username1)
        print("password",password)

        user = authenticate(username=username1,password=password)
        print("user line 61")
        if user is not None:
            login(request,user)
            return redirect("/home/")
        else:
            return render(request,"UserLogin.html",{"msg": "credentials not valid"})
    return render(request,"UserLogin.html")

@login_required
def home(request):
    c=0
    if request.method=="POST":
        title=request.POST.get("title","")
        content=request.POST.get("content","")
        print("request",request)
        print(dict(request.FILES))
        
        obj=Home()
        obj.title=title
        obj.content=content
        obj.save()
        
        c=1
        if c==1:
            return redirect('/display/')
        
        return render (request,'home.html',{"msg":"data submitted successfully","data1":obj}) 
    return render (request,'home.html')

@login_required
def display(request):
    data=Home.objects.all()
    data1=list(data)
    return render(request,"display.html",{"Home":data1[-4:]})


@login_required
def editdata(request,id):
    if(request.method=="POST"):
        title=request.POST.get("title","")
        content=request.POST.get("content","")

        home1=Home.objects.get(id=id)

        home1.title=title
        home1.content=content

        home1.save()
        return redirect('/display/')

    obj=Home.objects.filter(pk=id).first()


    return render(request,"edit.html",{"Home":obj})



@login_required
def deletedata(request,id):
    obj=Home.objects.get(id=id)
    obj.delete()
    return redirect('/display/')








        



