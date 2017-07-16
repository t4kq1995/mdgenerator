"""
mdgen URL Configuration
"""

from django.conf.urls import url
from mdgen import views

urlpatterns = [
    # Auth
    url(r'^auth_user/$', views.login),
]
