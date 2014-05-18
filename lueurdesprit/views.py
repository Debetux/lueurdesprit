from django.shortcuts import render
from django.http import HttpResponse
from work.models import TypeOfWork, Work, StaffReview
from blog.models import Entry

def home(request):
    latest_work_pub = Work.objects.all().exclude(staffreview__pk__isnull=True).order_by('-pk')[:4]
    latest_reviews_pub = StaffReview.objects.all().exclude(work__poster='').order_by('-pub_date')[:2]
    latest_news = Entry.objects.all()

    context = {
        'latest_work_pub': latest_work_pub,
        'latest_reviews_pub': latest_reviews_pub,
        'latest_news': latest_news,
    }
    return render(request, 'home/home.html', context)