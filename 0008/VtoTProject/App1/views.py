from django.shortcuts import render

# Create your views here.
def sample_view(request):
    return render(request, 'App1/sample.html')
