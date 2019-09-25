from django.conf.urls import *#patterns, include, url
from blogapp import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^addblog/', views.createBlog, name ="create"),
    url(r'^',views.index),
    url(r'^admin/', include(admin.site.urls)),

]
