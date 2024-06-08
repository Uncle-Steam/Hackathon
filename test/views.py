from django.shortcuts import render
from django.http import HttpResponse
import ai
import trialData

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
<<<<<<< HEAD
    
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
    name = request.GET['name']
    regisNumber = request.GET['regisNumber']
    foundedDate = request.GET['foundedDate']
    social = request.GET['social']
    
    concactenate = ""
    num = 1
    
    for i in trialData.users:
        concactenate += f"User {num} is planning to invest in {i['planning']}, is interested in {i['industry']} sectors, and follows {i['followed']} on LinkedIn.\n"
        num += 1
    
    prompt = f"You are analyzing a startup company and how likely they are to attract certain investor profiles based on their 
    About Us, objective, industry, name and their social cause. Here is their profile About Us:{about}, Objective:{objective}, Industry:{industry}, 
    Name:{name}, Social Cause:{social}. Make a compatibility analysis with the user profile provided which is: {concactenate}"
    
=======
    return render(request, 'signup.html')

def signup(request):
    context = {
        'title': "Sign Up"
    }
    return render(request, "signup.html", context)
>>>>>>> cae682711b303b118d48a2988521f36c655a026a
