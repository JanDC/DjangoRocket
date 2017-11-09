from django.conf.urls import include, url
from DjangoRocket.views import *

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^fire', fire, [], 'fire'),
    url(r'^move', move, [], 'move'),
    url(r'^abort', abort, [], 'abort'),
    url(r'^load', loadUp, [], 'load'),
    url(r'^files', files, [], 'files'),
    url(r'^$', home, [], 'home'),
]
