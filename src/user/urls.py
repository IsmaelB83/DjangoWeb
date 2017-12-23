# Python imports
# Django imports
from django.conf.urls import url
# Third party app imports
# Local app imports
from . import views


urlpatterns = [
    url(r'^profile/(?P<id>\d+)/$', views.profile, name='profile'),
    url(r'^settings/password/$', views.password, name='password'),
]
