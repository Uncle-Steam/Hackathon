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

types = [
    {'id': 1, 'name': 'Room One'},
    {'id': 2, 'name': 'Room Two'},
    {'id': 3, 'name': 'Room Three'},
]

def home(request):
    context = {
        'data': user,
        'types': types
    }
    return render(request, "test.html", context)

def about(request, pk):
    type = None
    for i in types:
        if i['id'] == int(pk):
            type = i
    context = {
        'type': type,
        'data': abouts
    }
    return render(request, "about.html", context)

def add(request):
    
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1+val2
    
    context = {
        'res': res
    }
    
    return render(request, 'about.html', context)