from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Entry

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def view_entry(request, slug):
    try:
        entry = Entry.objects.get(slug=slug)
    except Work.DoesNotExist:
        raise Http404
    return render(request, 'blog/detail.html', {'entry': entry})

def view_entry_in_category():
	pass
    
# Create your views here.
