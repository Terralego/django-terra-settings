Configuration
=============


In your project :

* settings

::

    INSTALLED_APPS = [
        ...
        # Utils app
        'terra_settings',
        ...
    ]


- SETTINGS :

Waiting for settings definition directly in models.

Settings should be overided  with TERRA_CRUD settings in your project settings file:

::

    TERRA_APPLIANCE_SETTINGS = {
        "title": "APP TITLE",
        # temp theme settings
        "theme": {
            "logo": {
                # base64
                "src": "data:image/png;##########################################",
                "alt": "ALT LOGO TEXT"
            },
        },
        # favicon settings
        # base64
        "favicon": "data:image/png;##########################################",
        # "landing_module": "CRUD",  optional, defined a landing module instead of select module landing page
    }

    FRONT_URL = 'http://localhost:3000'
    HOSTNAME = 'http://localhost:8000'
