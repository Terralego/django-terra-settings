Docker development
==================


To start a dev instance
"""""""""""""""""""""""

Define settings you wants in `test_terra_settings` django project.

``docker-compose up``

First start should failed as the database need to be initialized. Just launch
the same command twice.

Then initialize the database:

``docker-compose run --rm web /code/venv/bin/python3 /code/src/manage.py migrate``

You can now edit your code. A django runserver is launched internally so the
this is an autoreload server.

You can access to the api on http://localhost:8000/api/


Test
""""

To run test suite, just launch:

``docker-compose run --rm web /code/venv/bin/python3 /code/src/manage.py test``

