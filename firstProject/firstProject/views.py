from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Welcome to first Project: Home page</h1>")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("<h1>Welcome to first Project: About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to first Project: Contact page</h1>")