Local email testing plugin for tutor
=================================================================

This is a plugin for `Tutor <https://docs.tutor.edly.io>`_ for more convenient email testing using mailpit.

Installation
------------

::

  pip install tutor-contrib-mailpit

Usage
-----

Enable the plugin::

  tutor plugin enable mailpit

Save the changes in the environment::

    tutor config save

Run the environment::

    tutor dev start -d

Check the mailpit interface at http://localhost:8025 for outgoing emails.

Note that the plugin only works on in dev environment.
