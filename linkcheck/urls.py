from django.conf.urls.defaults import *

urlpatterns = patterns('linkcheck.views',
   url(r'^.*$', 'report', name="linkcheck-report"),
)