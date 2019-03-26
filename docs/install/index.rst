.. _weleup.install:

=======================
Installing Lino Welfare
=======================

See also http://www.lino-framework.org/dev/quick/install.html

Quick instructions
==================

Install from source::

    $ git clone https://github.com/lino-framework/weleup.git
    $ cd weleup
    $ virtualenv env
    $ . env/bin/activate
    $ pip install -e .

Then create a local project::

    $ mkdir mylino
    $ touch mylino/__init__.py
    $ nano mylino/settings.py

Add the following content to your :xfile:`settings.py` file::

    from lino_weleup.settings import *
    SITE = Site(globals())
    DEBUG = True

Tell Django and Python to use your settings::

    $ export DJANGO_SETTINGS_MODULE=mylino.settings
    $ export PYTHONPATH=.

Then initialize and populate the demo database::

    $ django-admin prep

And finally we launch a development server::

    $ django-admin runserver



