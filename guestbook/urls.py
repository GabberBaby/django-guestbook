from django.conf.urls import *

from views import EntryView

from models import Entry
from forms import EntryForm
from views import post_entry

list_dict = {'queryset': Entry.objects.filter(is_removed=False),
            'paginate_by': 5,
            'template_object_name': 'entry',
            'extra_context': {'form': EntryForm(), }}

last_page_dict = list_dict.copy()
last_page_dict.update({'page': 'last'})

page_dict = list_dict.copy()
page_dict.update({'allow_empty': False})

urlpatterns = patterns('',
    url(r'^$', EntryView.as_view(), last_page_dict, name='guestbook-page-last'),
    url(r'^page(?P<page>[0-9]+)/$', EntryView.as_view(), page_dict, name='guestbook-page'),
    url(r'^post/', post_entry, name='guestbook-post'),
)

