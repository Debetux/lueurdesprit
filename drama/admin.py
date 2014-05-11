from django.contrib import admin
from drama.models import Play, StaffReview

class PlayAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    fieldsets = [
        (None,               {'fields': ['title', 'description']}),
        ('Date information', {'fields': ['slug'], 'classes': ['grp-collapse grp-closed']}),
    ]

admin.site.register(Play, PlayAdmin)
admin.site.register(StaffReview)