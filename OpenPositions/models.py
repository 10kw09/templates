#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#OpenPosition page
class OpenPosition(models.Model):
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()