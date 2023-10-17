from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"mt1home.html")
def login(request):
    return render(request,"mtlogin.html")