================
django-guestbook
================
A simple guestbook application for Django
-----------------------------------------

What is it?
===========
Guestbook is a simple guestbook application for
the Django web-framework. It is closely based
on the contributed comments application.

Repo forked from https://github.com/dokterbob/django-guestbook and migrate to django 1.5.


Installation
============
#)  Get it from the Cheese Shop::
    
	easy_install django-guestbook
    
    **Or** get the latest & greatest from Github and link it to your
    application tree::
    
	git clone git://github.com/GabberBaby/django-guestbook.git
	ln -s django-guestbook/guestbook $PROJECT_DIR/guestbook
    
    (Here `$PROJECT_DIR` is your project root directory.)
    
#)  Add popularity to `INSTALLED_APPS` in settings.py::

	INSTALLED_APPS = (
	    ...
	    'guestbook',
	    ...
	)

#)  Create required data structure::

	cd $PROJECT_DIR
	./manage.py syncdb

#)  Add guestbook views to `urls.py`::

	urlpatterns += patterns('',
	    ...
	    (r'^guestbook/', include('guestbook.urls')),
	    ...
	)

#)  Enjoy!
