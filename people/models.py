from django.db import models
from django.db.models import permalink
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime
import os

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.title:
            filename = '{}.{}'.format(slugify(instance.title), ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper


class TypeOfPeople(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            if(self.slug):
                self.slug = slugify(self.slug)
            elif(len(self.title) >= 0):
                self.slug = slugify(self.title)

        super(TypeOfPeople, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Type of people'

class People(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    poster = models.ImageField(upload_to=path_and_rename('works/'), blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    type_of_people = models.ForeignKey(TypeOfPeople)

    def save(self, *args, **kwargs):

        if not self.id:
            # Newly created object, so set slug
            if(self.slug):
                self.slug = slugify(self.slug)
            else:
                self.slug = slugify('{} {}'.format(self.first_name, self.last_name))

        self.last_name = self.last_name.upper()

        super(People, self).save(*args, **kwargs)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)