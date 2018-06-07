"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from trips.views import hello_world, try2, home, go, math, emotion, comment
from trips.views import  try2, go, test, test2

urlpatterns = [

#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^hello/$', hello_world),
#     url(r'^(\d{1,2})/math/(\d{1,2})$',math),
#     url(r'^$', home),
#     url(r'^emotion$', emotion),
#     url(r'^comment$', comment),

     url(r'^try2/$', try2),
     url(r'^go$', go),
     url(r'^test$', test),
     url(r'^test2$', test2),
]
