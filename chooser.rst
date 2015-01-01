.. -*- rst -*-

=======
chooser
=======

----------------------------------------------
select which browser to use when opening a URI
----------------------------------------------

:Author: Lev Givon <lev@columbia.edu>
:Date: 2015-01-01
:Copyright: BSD
:Version: 0.3.3
:Manual section: 1

SYNOPSIS
========
**chooser** [*URI*]

DESCRIPTION
===========
**chooser** is a graphical utility that enables one to choose which web browser
to use when opening a URI. To invoke the utility when attempting to view a
selected URI via the mouse popup menu provided in many desktop environments, set 
your default web browser to 

**chooser** %s

CONFIGURATION
=============
By default, **chooser** searches for several common web browsers. One may also
specify which browsers to display in the configuration file
~/.config/chooser/chooserrc as follows:::

    [Browsers]
    Firefox: /usr/bin/firefox
    Chromium: /usr/bin/chromium-browser

SEE ALSO
========
**chromium-browser**\(1), **exo-open**\(1), **firefox**\(1)

BUGS
====
**chooser** might not recognize certain web browsers by default.
