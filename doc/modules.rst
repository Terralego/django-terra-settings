Map Base layers
===============

Define and manage map base layers

.. warning::
  * to enable BaseLayer module, you need to enable mapbox_baselayer in your INSTALLED_APPS

* API provide endpoints to get and manage map base layers

Get the list

* GET /api/baselayers

Get detail

* GET /api/baselayers/<slug>/

Delete

* DELETE /api/baselayers/<slug>/

UPDATE

* PUT /api/baselayers/<slug>/
* PATCH /api/baselayers/<slug>/

Create

* POST /api/baselayers/mapbox
* POST /api/baselayers/vector
* POST /api/baselayers/raster
