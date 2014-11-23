from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

     url(r'^fire/', 'DjangoRocket.views.fire', name='fire'),
     url(r'^move/', 'DjangoRocket.views.move', name='move'),
     url(r'^abort/', 'DjangoRocket.views.abort', name='abort'),
     url(r'^load/', 'DjangoRocket.views.loadUp', name='load'),
     url(r'^$', 'DjangoRocket.views.home', name='home'),
)
