

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from app2.models import post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def bloghome(request) :
    allpost=post.objects.all()
    
    
    context={"allpost":allpost}
    
    
        
          
    return render(request,"blogs.html",context)


def blogslug(request,slug) :
    Post=post.objects.filter(slug=slug)[0]
    
    
    context={"post":Post}
    
    
    print (post)
          
    return render(request,"blogslug.html",context)



def home(request) :
    print(request.user)
    #return HttpResponse("hallo home")
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"home.html")


def service(request) :
    #return HttpResponse("hallo sine")
    return render(request,"service.html")
def blog(request) :
    #return HttpResponse("hallo sine")
    if request.method=="POST":
        auther=request.POST.get("auther")
        tital=request.POST.get("tital")
        img=request.POST.get("img")
        slug=request.POST.get("slug")
        date=request.POST.get("date")
        containt=request.POST.get("containt")
        BLOG=post(auther=auther,tital=tital,img=img,containt=containt,slug=slug,date=date)
        BLOG.save()
        messages.success(request, 'your are sucssesfuly post blog')
        return render(request,"blog.html")

    
    
    return render(request,"blog.html")

def about(request) :
    #return HttpResponse("hallo about")
    return render(request,"about.html")
    

def loginuser(request) :
    #print(request.user)
    if request.method=="POST":
        #return HttpResponse("hallo images")
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user =authenticate(username=
username  , password= password  )
        #print(username,password)
        if user is not None:
            
            login(request, user)
            messages.success(request, 'your are sucssesfuly login')
            return redirect ("/")
            
            
        
        # A backend authenticated the credentials
        else:
            messages.success(request, 'wrong password or email adress')
            return render(request,"login.html")
            
    
    return render(request,"login.html")


def userlogout(request) :
    logout(request)
    messages.success(request, 'your are sucssesfuly logout')
    #return HttpResponse("hallo images")
    
    
       
    
        
    return render(request,"login.html")


def useraccount(request) :
    if request.method=="POST":
        
        if request.method=="POST":
            username = request.POST.get('username')
            useremail = request.POST.get("useremail")
            password = request.POST.get('password')
            Useraccount= User.objects.create_user(username,useremail,password)   
            
            
            Useraccount.save()
            
        
            return render(request,"home.html")
            messages.success(request, 'you are succsesfuly creat user')
        
        
        else:
            return HttpResponse("404 error")
    
        
    #return HttpResponse("hallo images")
    
    
       
    
        
    return render(request,"useraccount.html")

