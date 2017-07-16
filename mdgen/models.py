# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Member(models.Model):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return '%s (%s:%s)' % (self.name, self.login, self.password)
