from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'cloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^uploadfile/$', 'web.views.upload_file', name='upload_file'),
    #url(r'^index/$', 'web.views.index_page', name='index_page'),
    url(r'^success/$', 'web.views.success', name='success'),
]
