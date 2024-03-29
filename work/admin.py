from django.contrib import admin
from work.models import TypeOfWork, Work, StaffReview
from django.contrib.auth.models import User

class WorkAdmin(admin.ModelAdmin):
        # fields = ['title', 'description']

        list_display = ['type_of_work', 'title']

        fieldsets = [
            (None,               {'fields': ['type_of_work', 'title', 'description', 'website_url', 'poster']}),
            ('Advanced — Meta Data', {'fields': ['slug'], 'classes': ['grp-collapse grp-closed']}),
        ]

        class Media:
            js = [
                '/public/static/bower_components/tinymce/tinymce.min.js',
                '/public/static/js/tinymce_setup.js'
            ]

        

class StaffReviewAdmin(admin.ModelAdmin):
    list_display = ['work', 'pub_date', 'number_of_words', 'rating', 'author', 'published']

    fieldsets = [
        (None,               {'fields': ['work', 'body', 'opinion', 'rating', 'draft']}),
        ('Advanced — Meta Data', {'fields': ['title', 'slug', 'pub_date', 'author'], 'classes': ['grp-collapse grp-closed']}),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    class Media:
        js = [
            '/public/static/bower_components/tinymce/tinymce.min.js',
            '/public/static/js/tinymce_setup.js'
        ]

admin.site.register(TypeOfWork)
admin.site.register(Work, WorkAdmin)
admin.site.register(StaffReview, StaffReviewAdmin)