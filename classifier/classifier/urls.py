from django.conf import settings
from django.conf.urls import patterns, include, url
from view import home, processing, classifier, twitter_map, get_messages

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', home),
                       (r'^classifier/$', classifier),
                       (r'^processing/$', processing),
                       (r'^twitter_map/$', twitter_map),
                       (r'^get_messages/$', get_messages),
    # Examples:
    # url(r'^$', 'classifier.views.home', name='home'),
    # url(r'^classifier/', include('classifier.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    (r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root':settings.MEDIA_ROOT,}),
)
