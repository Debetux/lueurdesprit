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

def review_detail(request, type_of_work, work_slug, staffreview_id):
    try:
        review = StaffReview.objects.get(pk=staffreview_id)
    except Work.DoesNotExist:
        raise Http404
    return render(request, 'work/review.html', {'review': review})
    
def work_list(request, type_of_work):
    works = Work.objects.filter(type_of_work__slug=type_of_work)
    return render(request, 'work/work_list.html', {'works':works})

def staffreview_list(request, type_of_work):
    return HttpResponse("Hello, world. You're at the poll index.")


# Create your views here.
