from django.shortcuts import render,HttpResponse

# Create your views here.
def wish_view(request):
    return HttpResponse('Welcome to Django App')

def wish_me_view(request):
    return HttpResponse('Hi Surendra Welcome to Django App')

def thank_you_view(request):
    return HttpResponse('Thank you for visit our Django App')