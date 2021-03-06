django-linkcheck
================

.. image:: https://github.com/andybak/django-linkcheck/raw/master/linkcheck.jpg

A fairly flexible app that will analyze and report on links in any model that
you register with it. Links can be bare (urls or image and file fields) or
embedded in HTML (linkcheck handles the parsing). It's fairly easy to override
methods of the Linkcheck object should you need to do anything more
complicated (like generate URLs from slug fields etc).
 
You should run it's management command via cron or similar to check external
links regularly to see if their status changes. All links are checked
automatically when objects are saved. This is handled by signals.

Requirements
-----------

If you want the Ajax 'recheck' and 'ignore' buttons to work then JQuery should be available in your admin templates as $. (I intend to fix this so it works using the jQuery that Django loads automatically)

Basic usage
-----------

#. Install app to somewhere on your Python path

#. Add something along the lines of ``examples/linklists.py`` to every app that
   either:

  #) has models that contain content (e.g. url/image fields, chunks of markup
     or anything that gets transformed into a IMG or HREF when displayed
  #) can be the target of a link - i.e. is addressed by a url - in this case
     make sure it has an instance method named 'get_absolute_url'

#. Syncdb

#. Add to your root url config::

    (r'^admin/linkcheck/', include('linkcheck.urls')) 

#. View ``/admin/linkcheck/`` from your browser

The file 'notifications.py' is completely optional. It works with
admin-notifications_ to display a notification about broken links as
shown in the screenshot above.

.. _admin-notifications: http://github.com/andybak/django-admin-notifications

We are aware that this documentation is on the brief side of things so any
suggestions for elaboration or clarification would be gratefully accepted.

Settings
--------

LINKCHECK_RECHECK_INTERVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default: 10080 (1 week in minutes)

Will not recheck any link that has been checked more recently than this value.

LINKCHECK_EXTERNAL_REGEX_STRING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default: r'^https?://'

A string applied as a regex to a URL to determine whether it's internal or external.

LINKCHECK_MEDIA_PREFIX
~~~~~~~~~~~~~~~~~~~~~~

Default: '/media/'

Currently linkcheck tests whether links to internal static media are correct by wrangling the URL to be a local filesystem path.

It strips MEDIA_PREFIX off the interal link and concatenates the result onto settings.MEDIA_ROOT and tests that using os.path.exists

This 'works for me' but it is probably going to break for other people's setups. Patches welcome.

LINKCHECK_RESULTS_PER_PAGE
~~~~~~~~~~~~~~~~~~~~~~~~~~

Controls pagination.

Pagination is slightly peculiar at the moment due to the way links are grouped by object.


LINKCHECK_MAX_URL_LENGTH
~~~~~~~~~~~~~~~~~~~~~~~~

Default: 255

The length of the URL field. Defaults to 255 for compatibility with MySQL (see http://docs.djangoproject.com/en/dev/ref/databases/#notes-on-specific-fields )


SITE_DOMAIN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linkcheck treats all links as external because in certain situations, internal links fail to be checked properly. For example, when a django site is mounted on a specific path while files are mounted on another.

Linkcheck uses SITE_DOMAIN ex:

SITE_DOMAIN = "mysite.com"

django-filebrowser integration
------------------------------

If django-filebrowser is present on your path then linkcheck will listen to the post-upload, delete and rename signals and update itself according


Running tests
-------------

Tests can be run standalone by using the runtests.py script in linkcheck root:
    $ python runtests.py
If you want to run linkcheck tests in the context of your project, you should include 'linkcheck.tests.sampleapp' in your INSTALLED_APPS setting.
