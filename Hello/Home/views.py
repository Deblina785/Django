from unicodedata import name
from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages

def index(request):
    context={
        'variable':'chikki'
    }
    messages.success(request, 'this is a test message')
    return render(request,'test.html',context)
    # return HttpResponse('This is homepage')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('This is aboutpage')

def services(request):
    return render(request,'services.html')
    # return HttpResponse('This is servicepage')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        contact=Contact(name=name,address=address,city=city,state=state)
        contact.save()
        messages.success(request, 'Message sent')
        messages.error(request, 'Sorry some error occured')
    return render(request,'contact.html')
    # return HttpResponse('This is contactpage')
