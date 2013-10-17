from django.db import models
from django.utils import timezone
import datetime

class Publisher(models.Model):
  name = models.CharField(max_length=200)
  abbrev = models.CharField(max_length=30)
  impact_factor = models.DecimalField(max_digits=5, decimal_places=3)
  punkty_mnsw = models.IntegerField(default=0)
  website = models.URLField()

  def __unicode__(self):
    return self.abbrev
  
  class Meta:
    ordering = ('name',)

class Author(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  email = models.EmailField()

  def __unicode__(self):
    return u'%s %s' % (self.first_name, self.last_name)

  class Meta:
    ordering = []#('last_name',)

class Publication(models.Model):
  authors = models.ManyToManyField(Author)
  title = models.CharField(max_length=500)
  publisher = models.ForeignKey(Publisher)
  volume = models.IntegerField(default=0)
  page = models.CharField(max_length=10)
  pub_date = models.DateField()
  abstract = models.TextField(blank=True)
  doi = models.CharField(max_length=100,blank=True)
  www = models.URLField(blank=True)
  arxiv = models.CharField(max_length=20,blank=True)
  info = models.TextField(blank=True)

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ('-pub_date',)

  def was_published_this_year(self):
    dt = datetime.datetime.combine(self.pub_date, datetime.time(0,0))
    t = timezone.now()
    return dt > t.astimezone(timezone.utc).replace(tzinfo=None) - datetime.timedelta(days=365)
  was_published_this_year.admin_order_field = 'pub_date'
  was_published_this_year.boolean = True
  was_published_this_year.short_description = 'Published within a year?'
