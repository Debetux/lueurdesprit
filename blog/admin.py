from django.contrib import admin
from blog.models import Entry, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

class EntryAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'title']
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)