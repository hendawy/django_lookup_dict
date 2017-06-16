#Models for Django Lookup Dict App

# Django Lookup Dict is a django app that enables you use a django model
# the Python dict way.

# Copyright (C) 2014 Mohamed Hendawy

# This file is part of Django Lookup Dict.

from django.db import models


class Data_Store(models.Model):
    #Just another Key Value Lookup table
    dj_lookup_store_key = models.CharField(max_length=500)
    dj_lookup_store_value = models.CharField(max_length=500)

    def __str__(self):
        return "{0}: {1}".format(self.key, self.value) 

    def __repr__(self):
        return self.__str__(s)
