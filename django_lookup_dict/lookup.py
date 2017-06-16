# Django Lookup Dict is a django app that enables you use a django model
# the Python dict way.

# Copyright (C) 2014 Mohamed Hendawy

# This file is part of Django Lookup Dict.

from django_lookup_dict.models import Data_Store
from django.core.exceptions import MultipleObjectsReturned

class LookupDict(object):

    def __len__(self):
        return Data_Store.objects.count()

    def __getitem__(self, key):
        try:
            item = Data_Store.objects.get(dj_lookup_store_key = key)
            return item.dj_lookup_store_value
        except Data_Store.DoesNotExist:
            raise KeyError("Key '{0}' does not exist".format(key))
        except MultipleObjectsReturned:
            raise KeyError("Multiple entries for key: {0}".format(key))

    def __setitem__(self, key, value):
        try:
            item = Data_Store.objects.get(dj_lookup_store_key = key)
            item.dj_lookup_store_value = value
        except:
            item = Data_Store(dj_lookup_store_key = key, dj_lookup_store_value = value)
        item.save()

    def __delitem__(self, key):
        try:
            item = Data_Store.objects.get(dj_lookup_store_key = key)
            item.delete()
        except Data_Store.DoesNotExist:
            raise KeyError("Key '{0}' does not exist".format(key))
        except MultipleObjectsReturned:
            raise KeyError("Multiple entries for key: {0}".format(key))

    def __contains__(self, key):
        try:
            item = Data_Store.objects.get(dj_lookup_store_key = key)
            return True
        except Data_Store.DoesNotExist:
            return False
        except MultipleObjectsReturned:
            raise KeyError("Multiple entries for key: {0}".format(key))

    def delete(*args):
        Data_Store.objects.filter(dj_lookup_store_key__in = args).delete()
