from django.contrib import admin
from django.urls import path
from .views import *

from django.conf.urls import url

urlpatterns = [
    path(r'', begin_view),
    url(r'quiz/(?P<pk>[0-9]+)/$', question_view),
]