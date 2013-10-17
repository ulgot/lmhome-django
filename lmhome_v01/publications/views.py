from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from publications.models import Publication

def index(request):
  _list = Publication.objects.order_by('-pub_date')
  _nums = range(1,len(_list)+1)
  all_publications_dict = dict(zip(_nums[::-1],_list))
#  lfn = u'%s'%first_name
#  first_letters = "".join([i[:1]+"." for i in lfn.split(' ')])

  template = 'publications/index.html'
  context = {'all_publications_dict': all_publications_dict,}
  
  return render(request, template, context)

def detail(request, publication_id):
  try:
    publication = Publication.objects.get(pk=publication_id)
  except Publication.DoesNotExist:
    raise Http404
  return render(request, 'publications/detail.html', {'publication': publication})
