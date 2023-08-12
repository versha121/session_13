from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Home
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

def UserRegister(request):
    c=0
    if request.method =="POST":
        email=request.POST.get("email")
        fname=request.POST.get("fname")
        name=request.POST.get("name")
        Class=request.POST.get("Class")
        age=request.POST.get("age")
        gender=request.POST.get("gender")

        
        c=1

        if c==1:
            return redirect("/home/")



    

    return render (request,'UserRegister.html',{"msg":"User Registered Successfully"})


def UserLogin(request):
    if request.method=="POST":
        username=request.POST.get("email","")
        password =request.POST.get("password","")

        User = authenticate(username=username,password=password)
        if (User!=None):
            login(request,User)
            return redirect("/home/")
        else:
            return render(request,"Userlogin.html",{"msg": "credentials not valid"})
    return render(request,"Userlogin.html")

@login_required
def home(request):
    c=0
    if request.method=="POST":
        title=request.POST.get("title","")
        content=request.POST.get("content","")
        
        obj=Home()
        obj.title=title
        obj.content=content
        obj.save()
        c=1
        if c==1:
            return redirect('/display/')


        return render (request,'home.html',{"msg":"data submitted successfully"}) 
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



@login_required(login_url='/Userlogin/')
def deletedata(request,id):
    obj=Home.objects.get(id=id)
    obj.delete()
    return redirect('/display/')








        



