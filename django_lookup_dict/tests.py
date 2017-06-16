# Django Lookup Dict is a django app that enables you use a django model
# the Python dict way.

# Copyright (C) 2014 Mohamed Hendawy

# This file is part of Django Lookup Dict.


from django.test import TestCase
from django_lookup_dict import LookupDict


class LookupDictTestCase(TestCase):
    def setUp(self):
        self.lookup = LookupDict()

    def test_lookup(self):
        self.lookup['test1'] = 'test1'
        self.assertEqual(self.lookup['test1'], 'test1') #Looking up a key after setting it
        self.assertRaises(KeyError, lambda: self.lookup['itest2']) #Testing looking up key that doesn't exist

    def test_lookup_update(self):
        self.lookup['test1'] = 'test1'
        self.assertEqual(self.lookup['test1'], 'test1') #Looking up a key after setting it
        self.lookup['test1'] = 'test2'
        self.assertEqual(self.lookup['test1'], 'test2') #looking up a key after updating its value

    def test_lookup_contains(self):
        self.lookup['test1'] = 'test1'
        self.assertEqual('test1' in self.lookup, True) #testing a key that exists
        self.assertEqual('test2' in self.lookup, False) #testing a key that doesn't exist

    def test_lookup_length(self):
        self.assertEqual(len(self.lookup), 0) #Testing length before assigning any key to any value
        self.lookup['test1'] = 'test1'
        self.assertEqual(len(self.lookup), 1) #Testing after setting the first key.
        self.lookup['test2'] = 'test2'
        self.assertEqual(len(self.lookup), 2) #Testing after setting the second key.
