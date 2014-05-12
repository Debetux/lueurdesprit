from django.contrib import admin
from drama.models import Play, StaffReview
from django.contrib.auth.models import User

class PlayAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    fieldsets = [
        (None,               {'fields': ['title', 'description', 'poster']}),
        ('Advanced — Meta Data', {'fields': ['slug'], 'classes': ['grp-collapse grp-closed']}),
    ]

    def queryset(request):
        return User.objects.filter(author = request.user)

class StaffReviewAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['play', 'title', 'body', 'rating']}),
        ('Advanced — Meta Data', {'fields': ['slug', 'pub_date', 'author'], 'classes': ['grp-collapse grp-closed']}),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Play, PlayAdmin)
admin.site.register(StaffReview, StaffReviewAdmin)