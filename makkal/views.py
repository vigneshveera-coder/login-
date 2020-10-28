from django.shortcuts import render
from django.http import HttpResponse
from .models import post,securty


# Create your views here.

def index(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('password'):
            post=securty()
            post.name= request.POST.get('name')
            post.password= request.POST.get('password')
            post.save()
    #a=securty(name="karthi",password="ji")
    #a.save()
    #data=securty.objects.all()
    return render(request,'index.html',{})
    
