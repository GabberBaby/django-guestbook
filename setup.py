# This file is part of django-guestbook.
# 
# django-guestbook: A simple guestbook application for Django.
# Copyright (C) 2014 Igor Kupreev
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-guestbook',
    version = "0.2",
    description = 'A simple guestbook application for Django, based largely on the contributed comments application.',
    long_description = README,
    author = 'Mathijs de Bruin, gabberbaby',
    author_email = 'drbob@dokterbob.net, igorkupreev@gmail.com',
    url = 'https://github.com/GabberBaby/django-guestbook',
    packages = find_packages(),
    include_package_data = True,
    package_data={'forum':['templates/*.html', 'templates/forum/*.html','templates/forum/feeds/*.html']},
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
