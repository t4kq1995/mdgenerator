# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Member(models.Model):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return '%s (%s:%s)' % (self.name, self.login, self.password)
    

class CountryData(models.Model):
    country = models.CharField(max_length=10)
    data = models.TextField()
    
    def __str__(self):
        return '%s (%s)' % (self.country, True if len(self.data) > 0 else False)
    

class Country(models.Model):
    country = models.CharField(max_length=10)
    country_full = models.CharField(max_length=128)
    
    def __str__(self):
        return '%s | %s' % (self.country, self.country_full)


class UserData(models.Model):
    type = models.CharField(max_length=128)
    data = models.TextField()
    
    def __str__(self):
        return '%s (%s)' % (self.type, True if len(self.data) > 0 else False)
