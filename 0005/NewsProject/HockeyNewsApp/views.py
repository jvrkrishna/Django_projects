from django.shortcuts import render,HttpResponse

# Create your views here.
def hockey_view(r):
    return HttpResponse("This is Hockey View point")