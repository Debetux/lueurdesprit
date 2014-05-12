from django.shortcuts import render
from django.http import HttpResponse
from work.models import TypeOfWork, Work, StaffReview

def home(request):
    latest_work_pub = Work.objects.all()[:4]
    latest_reviews_pub = StaffReview.objects.all()[:2]
    context = {
        'latest_work_pub': latest_work_pub,
        'latest_reviews_pub': latest_reviews_pub
    }
    return render(request, 'home/home.html', context)