from django.contrib import admin
from people.models import *
from django.contrib.auth.models import User

class PeopleAdmin(admin.ModelAdmin):
        # fields = ['title', 'description']

        list_display = ['type_of_people', 'first_name', 'last_name']

        fieldsets = [
            (None,               {'fields': ['type_of_people', 'first_name', 'last_name', 'description', 'website_url', 'poster']}),
            ('Advanced — Meta Data', {'fields': ['slug'], 'classes': ['grp-collapse grp-closed']}),
        ]

        class Media:
            js = [
                '/public/static/bower_components/tinymce/tinymce.min.js',
                '/public/static/js/tinymce_setup.js'
            ]

admin.site.register(TypeOfPeople)
admin.site.register(People, PeopleAdmin)