"""planzz URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from planzz import views

from tastypie.api import Api
from django.contrib.auth.views import login, logout
from tastypie_user.resources import UserResource

v1_api = Api(api_name='v1')

v1_api.register(UserResource())

urlpatterns = [
    # url(r'^admin$', include(admin.site.urls)),
# url(r'^facebook$', include('django_facebook.urls')),
# url(r'^accounts$', include('django_facebook.auth_urls')),
    url(r'^$', views.index, name='index'),
    url(r'^signup$', views.signup),
    url(r'^login$', views.login),
    url(r'^schedule$', views.schedule),
    url(r'^signupprocess$', views.signupprocess),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
