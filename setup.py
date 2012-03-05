#!/usr/bin/env python

from setuptools import setup

NAME = 'chooser'
VERSION = '0.01'
AUTHOR = 'Lev Givon'
AUTHOR_EMAIL = 'lev@columbia.edu'
URL = 'HTTP://github.com/lebedov/chooser/'
DESCRIPTION = 'Choose browser when opening a URI'
LONG_DESCRIPTION = DESCRIPTION
LICENSE = 'BSD'
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: X11 Applications',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: BSD License',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Desktop Environment',
    'Topic :: Internet :: WWW/HTTP'
    ]

if __name__ == "__main__":
    setup(
        name = NAME,
        version = VERSION,
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        license = LICENSE,
        classifiers = CLASSIFIERS,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        url = URL,
        scripts = ['chooser'],
        install_requires = ['wxPython']
    )

