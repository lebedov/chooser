.. -*- rst -*-

Chooser
=======

Package Description
-------------------
`chooser` is a graphical utility that enables one to choose which 
web browser to use when opening a URI. To invoke the utility when attempting 
to view a selected URI, set your default web browser to

`chooser` \%s

Quick Start
-----------
Make sure that `wxPython <http://wxpython.org/>`_ is installed on your system.
If you have `pip <http://www.pip-installer.org/>`_ installed, run

    pip install chooser

You can also download the source tarball, unpack, and run

    python setup.py install

from within the source directory.

Configuration
-------------
By default, `chooser` searches for several common web browsers. One may also
specify which browsers to display in the configuration file
`~/config/chooser/chooserrc` as follows::

    [Browsers]
    Firefox: /usr/bin/firefox
    Chromium: /usr/bin/chromium-browser

Development
-----------
The latest source code can be obtained from `<http://github.com/lebedov/chooser/>`_.

Author
------
See the included AUTHORS.rst file for more information.

License
-------
This software is licensed under the 
`BSD License <http://www.opensource.org/licenses/bsd-license.php>`_.
See the included LICENSE.rst file for more information.
