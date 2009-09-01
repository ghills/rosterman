from django.conf.urls.defaults import *

urlpatterns = patterns('rosterman.roster.views',
    # Example:
    (r'^$', 'index'),
    (r'^(?P<team_id>\d+)/$', 'detail'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
