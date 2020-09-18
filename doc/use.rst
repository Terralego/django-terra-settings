How to use
==========

What is it
----------

django-terra-settings is a suite of tools used by terralego apps, but which can be used as standalone.
It aims to provide generic helpers that are used in a transversal way.


What it contains
----------------

Here is described each module content

terra_settings.helpers.responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

get_media_response()
""""""""""""""""""""

This method return a ``Response()`` object that contains
a file, or ``a X-Accel-Redirect`` header, depending of the ``MEDIA_ACCEL_REDIRECT`` setting.

This allow to implement internal redirection
with `X-Accel <https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/>`_
method to serve media files to end users.


terra_settings.management.commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

populatedata
""""""""""""

This is a generic management command, that try to execute, in a transaction, the function ``load_data`` of ``populate`` module of all installed app.

Those options are available:

 - ``-t`` : run load_test_data method instead
 - ``-d`` : run in dry mode
 - ``-l`` : list all available modules
 - ``-m`` : load data for only listed modules


terra_settings.templatetags.settings_tags
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A set of django template tags

front_url
"""""""""
Return the URL of the frontend (from ``FRONT_URL`` setting), generally needed in sent e-mail, as frontend is meant to be a React app.


hostname
""""""""
Return the URL of the ``HOSTNAME`` setting.

get_item(key)
"""""""""""""
Return the key content in a dict.


terra_settings.filters
^^^^^^^^^^^^^^^^^^^

DRF filter backends.

JSONFieldOrderingFilter
"""""""""""""""""""""""

Ordering filter for DRF, that permit to order from JSONField model content.
It works like Django model filters, using the ``__`` separator between parent child element.
Like this: ``field__dictkey1__subkey``


DateFilterBackend
"""""""""""""""""

DRF filter that allow to filter a queryset from date to date.
The usage through the API is like this:

``/my/api/endpoint?from_date=2000-01-01&to_date=2010-12-31``


terra_settings.mixins
^^^^^^^^^^^^^^^^^^^


MultipleFieldLookupMixin
""""""""""""""""""""""""

Mixin that allow DRF viewsets to use multiple lookup fields instead of just one. This allow, by example, to use the slug and the pk of a model to lookup an instance.

You must define a list of fields in the  ``lookup_fields`` attribute of the viewset.


SerializerCurrentUserMixin
""""""""""""""""""""""""""

Mixin to get current logged in users in serializer.

It provides a cached_property in the `current_user` attribute.


BaseUpdatableModel
""""""""""""""""""

Simple mixin that provide an abstract django model with two fields (``created_at``, ``updated_at``) to get creation and last update datetime.



terra_settings.pagination
^^^^^^^^^^^^^^^^^^^^^^

PagePagination
""""""""""""""

PageNumberPagination herited model that has default terralego pagination configuration.


terra_settings.views
^^^^^^^^^^^^^^^^^

SettingsView
""""""""""""

APIView that provides a set of configurations settings through a non-authenticated endpoint. This is used to provide initial configuration to frontend initialization.
