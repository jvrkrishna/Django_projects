from django.shortcuts import render
from .models import Contact

def contactus(request):
    return render(request,'contact_us.html')
def home(request):
    return render(request,'index.html')

def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['msg']
        data=Contact(name=name,email=email,message=message)
        data.save()
    return render(request,'contact_us.html')