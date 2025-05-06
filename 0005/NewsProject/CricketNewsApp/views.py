from django.shortcuts import render,HttpResponse

# Create your views here.
def cricket_view(r):
    return HttpResponse("This is Cricket View point")
