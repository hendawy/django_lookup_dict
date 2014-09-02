django-lookup-dict
========================

A django app that allows you to use a djanog model created by the app with a python dict-like operators. Useful for storing configuration variables


Hello, world
------------

**Simple Demo**::

	from django_lookup_dict import LookupDict

	lookup = LookupDict()
	lookup['hello'] = 'world'
	print "Lookup for Hello is : {0}".format(lookup['hello'])


How To:
------------

Setting a value, regular assigningment with the square bracket operator [ ]::

	lookup['hello'] = 'world'

Retrieving a value, using square bracket operator [ ]::

	lookup['hello']

Key count::

	len(lookup)

Deletin, using the del and using square bracket operators::

	del lookup['hello']

Deleting certain keys::

	# lookup.delete(*args)
	lookup.delete('key1', 'key2', 'key3')

Installation
------------

**Automatic installation**::

	pip install django_lookup_dict

**Manual installation**: Download the latest source from `GitHub 
<https://github.com/hendawy/django_lookup_dict/releases>`_.

.. parsed-literal::

	tar xvzf django_lookup_dict-[VERSION].tar.gz
	cd django_lookup_dict-[VERSION]
	python setup.py build
	sudo python setup.py install

**After Instalation**:

	#.	Add 'django_lookup_dict' to INSTALLED_APPS in your django project's settings.
	#.	Run 'python manage.py syncdb' in order to create the data storage for the model.
