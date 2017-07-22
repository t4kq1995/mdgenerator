"""
mdgen URL Configuration
"""

from django.conf.urls import url
from mdgen import views

urlpatterns = [
    # Auth
    url(r'^auth_user/$', views.login),
    # Get country
    url(r'^get_country/$', views.get_country_full),
    # User data
    url(r'^get_user_data/$', views.get_user_data),
    # Country data
    url(r'^get_country_data/$', views.get_country_data),
]
