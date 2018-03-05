from django.conf.urls import include, url
from django.contrib import admin 
from django.urls import path 
from . import views

urlpatterns = [ 
	path('', views.index, name='index'), 

    # Examples:
    # url(r'^$', 'new_test_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')), 
    

    url(r'^admin/', include(admin.site.urls)),
]
