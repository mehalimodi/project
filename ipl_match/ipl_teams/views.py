from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"ipl_teams/index.html")

def about1(request):
    return render(request,"ipl_teams/about1.html")

def about2(request):
    return render(request,"ipl_teams/about2.html")

def about3(request):
    return render(request,"ipl_teams/about3.html")

def about4(request):
    return render(request,"ipl_teams/about4.html")

def about5(request):
    return render(request,"ipl_teams/about5.html")

def about6(request):
    return render(request,"ipl_teams/about6.html")

def about7(request):
    return render(request,"ipl_teams/about7.html")