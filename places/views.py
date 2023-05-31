from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"places/index.html",{"Title": "Главная страница"})
def profile(request):
    return render(request,"places/profile.html",{"Title": "Профиль"})
# def index(request):
#     return HttpResponse("HERE")
