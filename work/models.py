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


class TypeOfWork(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            if(self.slug):
                self.slug = slugify(self.slug)
            elif(len(self.title) >= 0):
                self.slug = slugify(self.title)

        super(TypeOfWork, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Type d’œuvre'
        verbose_name_plural = 'Types d’œuvre'

class Work(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    poster = models.ImageField(upload_to=path_and_rename('works/'), blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    type_of_work = models.ForeignKey(TypeOfWork)

    def save(self, *args, **kwargs):

        if not self.id:
            # Newly created object, so set slug
            if(self.slug):
                self.slug = slugify(self.slug)
            elif(len(self.title) >= 0):
                self.slug = slugify(self.title)

        super(Work, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Œuvre'
        verbose_name_plural = 'Œuvres'



class StaffReview(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    body = models.TextField()
    opinion = models.TextField(blank=True, null=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
    rating = models.IntegerField()
    pub_date = models.DateTimeField(blank=True)
    author = models.ForeignKey(User, null=True, blank=True)
    work = models.ForeignKey(Work)
    draft = models.BooleanField()

    def save(self, *args, **kwargs):
        if(len(self.title) >= 0):
            self.slug = slugify(self.work.title)
        else:
            self.slug = slugify(self.work.title)

        ''' On save, update timestamps '''
        if not self.id:
            self.pub_date = datetime.datetime.today()

        super(StaffReview, self).save(*args, **kwargs)

    def __str__(self):
        return self.work.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def published(self):
        if self.draft == False:
            return True
        else:
            return False

    published.boolean = True
    published.admin_order_field = 'draft'
    published.short_description = 'Published ?' 

    def number_of_words(self):
        return len(self.body.split() + self.opinion.split())

    number_of_words.short_description = 'Nombre de mots de la critique'

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)

    class Meta:
        verbose_name = 'Critique'
        verbose_name_plural = 'Critiques'