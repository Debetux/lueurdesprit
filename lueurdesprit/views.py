from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = None
    return render(request, 'home/home.html', context)