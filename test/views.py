from django.shortcuts import render, redirect
from django.http import HttpResponse
from test import ai
from test import trialData
import ast

user = {
    'username': 'Tritop21',
    'type': 'Startup'
}


def index(request):
    context = {
        'data': index,
        'title': "Login"
    }
    return render(request, "index.html", context)

def investor(request):
    return render(request, "dashboard-investor.html")

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

def sortUser(arrayUser):
    sorted_arrayUser = sorted(arrayUser, key=lambda x: int(x[1].replace('%', '')), reverse=True)
    return sorted_arrayUser

def generate(about, industry, name, social):
    concactenate = ""
    num = 1
    
    for i in trialData.users:
        concactenate += f"User {num} is planning to invest in {i['planning']}, is interested in {i['industry']} sectors, and follows {i['followed']} on LinkedIn.\n"
        num += 1
    
    prompt = f"""You are analyzing a startup company and how likely they are to attract certain investor profiles based on their 
    About Us, objective, industry, name and their social cause. Here is their profile About Us:{about}, Industry:{industry}, 
    Name:{name}, Social Cause:{social}. Make a compatibility analysis with the user profile provided which is: {concactenate}. Make the result in 
    this format and do it for all user, use a csv format output that only includes user number, compatibility percentage and a reasoning less than 15 words
    do not have any preface sentences, and separate each user analysis with a comma instead of a space, make the reasoning more interesting and do not use vocabulary 'focus', 'interest'"""
    
    unSplit = ai.assistant(prompt)
    array = unSplit.split(",")

    textList = []
    text = []
    for i, item in enumerate(array):
        item = item.replace("\n", "")
        if (i + 1) % 3 != 0:
            text.append(item)
        else:
            text.append(item)
            textList.append(text)
            text = []
    
    sortedResult = sortUser(textList)
    
    return sortedResult

def dashboard(request):
    about = request.GET['about']
    industry = request.GET['industry']
    name = request.GET['name']
    regisNumber = request.GET['regisNumber']
    foundedDate = request.GET['foundedDate']
    social = request.GET['social']
    result2_str = request.GET['result2']
    
    try:
        result2 = ast.literal_eval(result2_str)
    except:
        result2 = []

    context = {
            'about': about,
            'industry': industry,
            'name': name,
            'regisNumber': regisNumber,
            'foundedDate': foundedDate,
            'social': social,
            'result': result2
        }

    return render(request, 'dashboard-startup.html', context)

def insight(request):
    about = request.GET['about']
    industry = request.GET['industry']
    name = request.GET['startup__name']
    regisNumber = request.GET['reg__no']
    foundedDate = request.GET['found__date']
    social = request.GET['objective']
    
    insightResult = insightGen(about, industry, name, social)
    genResult = generate(about, industry, name, social)
    
    context = {
            'about': about,
            'industry': industry,
            'name': name,
            'regisNumber': regisNumber,
            'foundedDate': foundedDate,
            'social': social,
            'result1': insightResult,
            'result2': genResult
        }
    
    return render(request, 'insights.html', context)

def insightGen(about, industry, name, social):
    prompt = f"""You are analyzing a startup company and how likely they are to attract certain investor profiles based on their 
    About Us, objective, industry, name and their social cause. Here is their profile About Us:{about}, Industry:{industry}, 
    Name:{name}, Social Cause:{social}. Rate them out of 10 in the following criterias 1. Scalability 2. Market Size 3. Social Cause
    4. Competitive Landscape. Make the result in this format: 'number,number,number,number,reasoning on criteria', use a csv format output, 
    do not have any preface sentences whatsoever, answer needs to start with the format given"""
    
    unSplit = ai.assistant(prompt)
    result = unSplit.split(",")
    
    return result