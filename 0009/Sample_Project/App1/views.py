from django.shortcuts import render
from .models import Post
# Create your views here.
def App1_view(request):
    posts=Post.objects.all()
    return render(request,'App1/App1_home.html',{'posts':posts})