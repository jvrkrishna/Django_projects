from django.shortcuts import render,HttpResponse

# Create your views here.
def course_view(r):
    return HttpResponse("Hello This is Course View.")