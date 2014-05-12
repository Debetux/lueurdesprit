from django.contrib import admin
from blog.models import Entry, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Advanced — Meta Data', {'fields': ['slug'], 'classes': ['grp-collapse grp-closed']}),
    ]


class EntryAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'title']
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']

    fieldsets = [
        (None,               {'fields': ['title', 'body', 'category']}),
        ('Advanced — Meta Data', {'fields': ['slug', 'pub_date', 'author'], 'classes': ['grp-collapse grp-closed']}),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)