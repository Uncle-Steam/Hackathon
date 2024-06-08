from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response (handler)

user = {
    'username': 'Tritop21',
    'type': 'Startup'
}

abouts = {
    'cocreators': ['Ananda', 'Averil', 'Janson', 'Weipin', 'Winsen']
}


def index(request):
    context = {
        'data': index,
        'title': "Login"
    }
    return render(request, "index.html", context)


def login(request):
    
    defaultUser = "Tritop21"
    defaultPass = "password123"
    
    user = request.GET['username']
    password = request.GET['password']
    
    if user == defaultUser and password == defaultPass:
        return render(request, 'signup.html')
    else:
        return render(request, 'index.html')
    