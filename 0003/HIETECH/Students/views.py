from django.shortcuts import render,HttpResponse

# Create your views here.
def student_view(r):
    return HttpResponse("Hello This is Student View.")