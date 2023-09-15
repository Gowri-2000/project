from django.shortcuts import render
from django.http import HttpResponse
from .models import logindata
from pathlib import Path
import os
# Create your views here.
def home(request):
    msg="<h1>hello</h1>"
    return HttpResponse(msg)

def sample_without_variable(request):
    return render(request,"myfirst.html")

def sample_with_variable(request):
    name='karthi'
    return render(request,"myfirst.html",{'name':'karthi'})

# def login(request):
#     if request.method=='POST':
#         username=request.POST['user']
#         password=request.POST['pass']
        
#         obj=logindata()
#         obj.username=username
#         obj.password=password
#         obj.save()
#         return render(request,"thankyou.html")

#     return render(request,"login.html")

def loginresponse(request):
    username=request.POST['user']
    password=request.POST['pass']
    return render(request,"loginresponse.html",{'user':username,'pass': password})

def treeresponse(request):
    return render(request,"treeresponse.html")

def thankyoucall(request):
    return render(request,"thankyou.html")



def login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']
        
        obj=logindata()
        obj.username=username
        obj.password=password
        obj.save()
        d=logindata.objects.all()
        return render(request,"login.html",{'datas':d})

    return render(request,"login.html")

