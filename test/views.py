from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request -> response (handler)

def hello(request):
    return render(request, "test.html")