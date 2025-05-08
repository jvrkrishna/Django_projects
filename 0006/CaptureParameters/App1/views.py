from django.shortcuts import render,HttpResponse

# Create your views here.
def display_id(request,id):
    return HttpResponse(id)

def display_name(request,name):
    return HttpResponse(f"My name is {name}")