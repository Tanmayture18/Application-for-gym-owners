from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from tans.models import Services
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("homepage")
    return render(request,'index.html')
def about(request):
    # return HttpResponse("aboutpage")
    return render(request,'about.html')
def services(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        services=Services(name=name,email=email,phone=phone,desc=desc)
        services.save()
        messages.success(request, 'your request has beem submitted')
        
    # return HttpResponse("servicespage")
    return render(request,'services.html')
def contact(request):
    # return HttpResponse("contactpage") 
    return render(request,'contact.html')          