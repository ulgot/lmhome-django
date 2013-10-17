from django.contrib import admin
from publications.models import Publisher, Publication

class PublicationAdmin(admin.ModelAdmin):
  fieldsets = [
      (None, {'fields': ['title']}),
      ('Authors', {'fields': ['authors']}),#, 'classes': ['collapse']}),
      ('Publisher', {'fields': ['publisher','volume','page','pub_date','pdf']}),#, 'classes': ['collapse']}),
      ('Abstract', {'fields': ['abstract'], 'classes': ['collapse']}),
      ('URLs', {'fields': ['doi','arxiv','www']}),
      ('Additional info', {'fields': ['info'], 'classes': ['collapse']}),
      ]
  list_display = ('title', 'pub_date', 'was_published_this_year')
  list_filter = ['pub_date']
  search_field = ['title']
  date_hierarchy = 'pub_date'

admin.site.register(Publication, PublicationAdmin)
admin.site.register(Publisher)

