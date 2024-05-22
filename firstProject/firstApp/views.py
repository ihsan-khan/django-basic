from django.shortcuts import render

# Create your views here.from django.shortcuts import render

def all_blogs(request):
    # return HttpResponse("<h1>Welcome to first Project: Home page</h1>")
    return render(request,'firstApp/all_blogs.html')

