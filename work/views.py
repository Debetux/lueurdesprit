from django.shortcuts import render
from django.http import HttpResponse
from work.models import *
from django.http import Http404

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def work_detail(request, type_of_work, slug):
    try:
        work = Work.objects.get(slug=slug)
    except Work.DoesNotExist:
        raise Http404
    return render(request, 'work/detail.html', {'work': work})

def review_detail(request, type_of_work, slug):
    try:
        review = StaffReview.objects.get(slug=slug)
    except Work.DoesNotExist:
        raise Http404
    return render(request, 'work/review.html', {'review': review})
    
# Create your views here.
