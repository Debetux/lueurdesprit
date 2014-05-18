from django.shortcuts import render
from django.http import HttpResponse
from work.models import TypeOfWork, Work, StaffReview
from blog.models import Entry

def home(request):
    """ Useless, for now """
    # latest_work_pub = Work.objects.all().exclude(staffreview__pk__isnull=True).order_by('-pk')[:4]
    # latest_reviews_pub = StaffReview.objects.all().exclude(work__poster='').order_by('-pub_date')[:2]
    latest_news = Entry.objects.all()

    latest_staffreviews_theatre = Work.objects.filter(type_of_work__slug="piece-de-theatre").exclude(staffreview__pk__isnull=True).order_by('-pk')[:4]
    latest_staffreviews_book = Work.objects.filter(type_of_work__slug="litterature").exclude(staffreview__pk__isnull=True).order_by('-pk')[:4]
    latest_staffreviews_cinema = Work.objects.filter(type_of_work__slug="cinema").exclude(staffreview__pk__isnull=True).order_by('-pk')[:4]
    latest_staffreviews_music = Work.objects.filter(type_of_work__slug="musique").exclude(staffreview__pk__isnull=True).order_by('-pk')[:4]

    context = {
        # 'latest_work_pub':              latest_work_pub,
        # 'latest_reviews_pub':           latest_reviews_pub,
        'latest_news':                  latest_news,
        'latest_staffreviews_theatre':  latest_staffreviews_theatre,
        'latest_staffreviews_cinema':   latest_staffreviews_cinema,
        'latest_staffreviews_book':     latest_staffreviews_book,
        'latest_staffreviews_music':    latest_staffreviews_music,
    }
    return render(request, 'home/home.html', context)