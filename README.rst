Overview
========

.. image:: https://secure.travis-ci.org/osupython/pip2.png?branch=develop
    :target: http://travis-ci.org/osupython/pip2

The goal of this project is to create a new version of `pip`_ built on
`Distutils2/packaging`_ instead of setuptools/distribute. Pip2 currently
provides very minimal install, uninstall, search and freeze commands that use
Distutils2/packaging under the hood. Note that this project is still in the
early stages of development and is nowhere near ready for serious use.

Rather than starting as a fork of the pip codebase, pip2 was written from
scratch to avoid the unmaintainable mess that would likely result from trying
to add Distutils2/packaging support to pip while maintaining backwards
compatibility.

Pip2 was originally developed as part of a 2011-2012 senior capstone project
at Oregon State University. To limit the scope of the student project, we
avoided areas that required deep understanding of the Python packaging
ecosystem. We chose not to go too far into the details of Distutils2 as it was
still under heavy development and not ready for prime time. We also tried not
to make important design decisions for pip2.

Instead, our goal was to create a solid, well-tested foundation with very
basic functionality that can be handed off to the pip maintainers for further
development. We wanted to keep it simple, get something working and tested,
let people play with it, and then improve it from there.

Note that only Python 3.2 is supported at this time.

.. _pip: http://www.pip-installer.org/
.. _Distutils2/packaging: http://pypi.python.org/pypi/Distutils2

Contributing
============

See the `pip2 contribution instructions`_ for details on setting up a
development environment and contributing to pip2.

A list of known issues can be found in the `pip2 issue tracker`_.

.. _pip2 contribution instructions: http://pip2.readthedocs.org/en/latest/dev/contributing.html
.. _pip2 issue tracker: https://github.com/osupython/pip2/issues

Installation
============

Since pip2 and the supporting packaging libraries are nowhere near stable, you
should create a virtual environment to experiment with it::

    $ virtualenv --python=python3.2 pip2
    $ source pip2/bin/activate

Install Distutils2 and pip2::

    $ pip install http://hg.python.org/distutils2/archive/python3.tar.bz2
    $ pip install git+https://github.com/osupython/pip2.git

Usage
=====

The following commands are currently supported. Since Distutils2/packaging
aims to maintain backwards compability, these commands should work on projects
that are packaged with Distutils2/packaging as well as with other libraries
such as distutils, setuptools, and distribute.

Install
-------

Install one or more projects.

Usage: ``pip2 install <project>...``

Projects can be installed from the `Python Packaging Index (PyPI)`_::

    $ pip2 install TowelStuff sample_distutils2_project
    Successfully installed TowelStuff, sample_distutils2_project.

.. _Python Packaging Index (PyPI): http://pypi.python.org/pypi

Projects can also be installed from local archives (.zip, .tar.gz, .tar.bz2,
.tgz, or .tar) or directories::

    $ pip2 install sample_distutils2_project.tar.gz
    Successfully installed sample_distutils2_project.tar.gz

    $ pip2 install /path/to/TowelStuff
    Successfully installed /path/to/TowelStuff.

Freeze
------

Display a list of installed projects with their version.

Usage: ``pip2 freeze``

Example::

    $ pip2 freeze
    TowelStuff==0.1.1
    sample_distutils2_project==1.1.0


Search
------

Search the Python Package Index (PyPI).

Usage: ``pip2 search <query>``

Example::

    $ pip2 search pyglet
    snowui                     - snowui is a fast and simple GUI using
                                 pyglet and rabbyt.
    svgbatch                   - Loads SVG files into pyglet Batch objects
                                 for OpenGL rendering.
    kytten                     - GUI Framework for Pyglet
    Fungus                     - A simple scene based game engine building
                                 on pyglet.

Uninstall
---------

Uninstall one or more projects.

Usage: ``pip2 uninstall <project>...``

Example::

    $ pip2 uninstall sample_distutils2_project
    Successfully uninstalled sample_distutils2_project.

As a Library
------------

The pip2 commands can also be used as a library with parameters that match
those used on the command line. For example::

    >>> from pip2.commands.install import install
    >>> install(['TowelStuff', 'sample_distutils2_project'])
    {'failed': [], 'installed': ['TowelStuff', 'sample_distutils2_project']}

    >>> from pip2.commands.freeze import freeze
    >>> freeze()
    {'TowelStuff': {'version': '0.1.1'},
     'sample_distutils2_project': {'version': '1.1.0'}}

See the `API Reference`_ for details.

.. _API Reference: http://pip2.readthedocs.org/en/latest/dev/api/index.html
