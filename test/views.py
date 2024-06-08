from django.shortcuts import render
from django.http import HttpResponse
from test import ai
from test import trialData

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

def signup(request):
    context = {
        'title': "Sign Up"
    }
    return render(request, "signup.html", context)

def login(request):

    defaultUser = "Tritop21"
    defaultPass = "password123"
    
    user = request.GET['username']
    password = request.GET['password']
    
    if user == defaultUser and password == defaultPass:
        return render(request, 'signup.html')
    else:
        return render(request, 'index.html')


def firstGenerate(request):
    about = request.GET['about']
    objective = request.GET['objective']
    industry = request.GET['industry']
    name = request.GET['startup__name']
    regisNumber = request.GET['reg__no']
    foundedDate = request.GET['found__date']
    social = request.GET['objective']
    
    concactenate = ""
    num = 1
    
    for i in trialData.users:
        concactenate += f"User {num} is planning to invest in {i['planning']}, is interested in {i['industry']} sectors, and follows {i['followed']} on LinkedIn.\n"
        num += 1
    
    prompt = f"""You are analyzing a startup company and how likely they are to attract certain investor profiles based on their 
    About Us, objective, industry, name and their social cause. Here is their profile About Us:{about}, Objective:{objective}, Industry:{industry}, 
    Name:{name}, Social Cause:{social}. Make a compatibility analysis with the user profile provided which is: {concactenate}. Make the result in 
    this format and do it for all user, use a csv format output that only includes user number, compatibility percentage and a reasoning less than 15 words"""
    
    result = ai.assistant(prompt)

    return render(request, 'test.html', {'result': result})

