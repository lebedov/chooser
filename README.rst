.. -*- rst -*-

Chooser
=======

Package Description
-------------------
`chooser` is a graphical utility that enables one to choose which 
web browser to use when opening a URI. 

.. image:: https://img.shields.io/pypi/v/chooser.svg
    :target: https://pypi.python.org/pypi/chooser
    :alt: Latest Version
    
Quick Start
-----------
Make sure that `pyxdg <http://freedesktop.org/wiki/Software/pyxdg/>`_ and 
`wxPython <http://wxpython.org/>`_ are installed on your system.
If you have `pip <http://www.pip-installer.org/>`_ installed, run::

    pip install chooser

You can also download the source tarball, unpack, and run::

    python setup.py install

from within the source directory.

To invoke the utility when attempting to view a selected URI via the mouse popup 
menu provided in many desktop environments, set your default web browser to::

    chooser "%s"

Configuration
-------------
By default, `chooser` searches for several common web browsers. One may also
specify which browsers to display in the configuration file
`~/.config/chooser/chooserrc` as follows::

    [Browsers]
    Firefox: /usr/bin/firefox
    Chromium: /usr/bin/chromium-browser

Development
-----------
The latest source code may be obtained from `GitHub 
<http://github.com/lebedov/chooser/>`_.

Author
------
See the included `AUTHORS.rst
<https://github.com/lebedov/chooser/blob/master/AUTHORS.rst>`_ file for more
information.

License
-------
This software is licensed under the `BSD License
<http://www.opensource.org/licenses/bsd-license>`_.  See the included
`LICENSE.rst <https://github.com/lebedov/chooser/blob/master/LICENSE.rst>`_ file
for more information.
