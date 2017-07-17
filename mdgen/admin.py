# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mdgen.models import Member, Country, CountryData

admin.site.register(Member)
admin.site.register(CountryData)
admin.site.register(Country)
