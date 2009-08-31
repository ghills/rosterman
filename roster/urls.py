from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    (r'^roster/', include('rosterman.roster.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
