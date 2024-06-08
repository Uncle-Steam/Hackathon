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
    return render(request, 'signup.html')


def signup(request):
    context = {
        'title': "Sign Up"
    }
    return render(request, "signup.html", context)
