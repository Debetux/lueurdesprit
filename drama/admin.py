from django.contrib import admin
from drama.models import Play, StaffReview

class PlayAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    fieldsets = [
        (None,               {'fields': ['title', 'description', 'poster']}),
        ('Advanced — Meta Data', {'fields': ['slug'], 'classes': ['grp-collapse grp-closed']}),
    ]

admin.site.register(Play, PlayAdmin)
admin.site.register(StaffReview)