from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

user = {
        'username': 'Tritop21',
        'type': 'Startup'
    }

abouts = {
    'cocreators': ['Ananda', 'Averil', 'Janson', 'Weipin', 'Winsen']
}

def home(request):
    context = {
        'data': user
    }
    return render(request, "test.html", context)

def about(request):
    context = {
        'data': abouts
    }
    return render(request, "about.html", context)