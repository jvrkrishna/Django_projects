from django.shortcuts import render

# Create your views here.
def sample_view(request):
    data = {
        'name': 'Alice',
        'age': 30,
        'items': ['Apples', 'Bananas', 'Cherries']
    }
    return render(request, 'App1/sample.html', context=data)
