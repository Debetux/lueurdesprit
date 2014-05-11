from django.db import models
from django.db.models import permalink
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Play(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField()

class StaffReview(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    rating = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, limit_choices_to={'is_staff': True})
    play = models.ForeignKey(Play)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        verbose_name_plural = 'Staff Reviews'