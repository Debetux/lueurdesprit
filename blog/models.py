from django.db import models
from django.db.models import permalink
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

class Entry(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(blank=True)
    author = models.ForeignKey(User, limit_choices_to={'is_staff': True}, blank=True, null=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
            ''' On save, update timestamps '''
            self.pub_date = datetime.datetime.today()

        super(Entry, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Entries'