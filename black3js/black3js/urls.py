from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'black3js.views.home', name='home'),
    # url(r'^black3js/', include('black3js.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),

    #media
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the next line to enable the admin:
	url(r'^$', 'black3js.views.home', name="home"),
    url(r'^chart/', 'game.views.chart', name='chart'),    
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^api/', include('game.urls')),
    

    #url(r'line/^$', game.views.index, name='index'),    
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
