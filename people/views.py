from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

def index(request):
    return HttpResponse("Hello, world. You're at the people index.")