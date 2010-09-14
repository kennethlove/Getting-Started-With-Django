from django.conf.urls.defaults import *
from django.views.generic import list_detail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Blog

blog_info = {
    "queryset": Blog.objects.filter(active=True),
}

urlpatterns = patterns('',
    # Example:
    # (r'^tumblog/', include('tumblog.foo.urls')),
    url(r'^$', list_detail.object_list, blog_info, name="home"),
    url(r'^blog/(?P<slug>[-\w]+)/$', 'blog.views.blog', name="blog"),
    url(r'^blog/(?P<slug>[-\w]+)/(?P<y>\d{4})/$', 'blog.views.year', name="year"),
    url(r'^blog/(?P<slug>[-\w]+)/(?P<y>\d{4})/(?P<m>\d{2})/$', 'blog.views.month', name="month"),

    url(r'^blog/(?P<blog>[-\w]+)/post/(?P<slug>[-\w]+)/$', 'blog.views.post', name="post"),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Sites/tutorial/public/media'}),
)
