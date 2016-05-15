# Django Lookup Dict is a django app that enables you use a django model
# the Python dict way.

# Copyright (C) 2014 Mohamed Hendawy

# This file is part of Django Lookup Dict.

# Django Lookup Dict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Django Lookup Dict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

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
