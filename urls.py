"""archive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import archive.views


urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^tags/(?P<tag_name>\w+)',archive.views.tags, name='tag'),

	url(r'^$', archive.views.index, name='index'),
	url(r'^(?P<year_name>\w+)/(?P<slot_slug>[^/]+)',archive.views.slot, name='slot'),
	url(r'^(?P<year_name>\w+)',archive.views.year, name='year'),


]

'''
url(r'^tags',archive.views.tags, name='tags'),

'''
