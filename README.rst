Overview
========

.. image:: https://secure.travis-ci.org/osupython/pip2.png?branch=develop
    :target: http://travis-ci.org/osupython/pip2

The goal of this project is to create a new version of pip built on
`distutils2/packaging`_ instead of setuptools/distribute. Pip2 is currently
being developed as part of a senior capstone project at Oregon State
University.

Rather than starting as a fork of the pip codebase, pip2 was written from
scratch to avoid the unmaintainable mess that would likely result from trying
to add distutils2/packaging support to pip while maintaining backwards
compatibility. Our goal is to create a solid, well-tested foundation with very
basic functionality that can be handed off to the pip maintainers for further
development. Pip2 currently provides minimal install, uninstall, search and
freeze commands that use distutils2/packaging under the hood.

Note that only Python 3.2 is supported at this time.

.. _distutils2/packaging: http://pypi.python.org/pypi/Distutils2

Contributing
============

See the `pip2 contribution instructions`_ for details on setting up a
development environment and contributing to pip2.

.. _pip2 contribution instructions: http://pip2.readthedocs.org/en/latest/dev/contributing.html

Installation
============

Since pip2 and the supporting packaging libraries are nowhere near stable, you
should create a virtual environment to experiment with it::

    $ virtualenv --python=python3.2 pip2
    $ source pip2/bin/activate

Install distutils2 and pip2::

    $ pip install http://hg.python.org/distutils2/archive/python3.tar.bz2
    $ pip install git+https://github.com/osupython/pip2.git

Usage
=====

The following commands are currently supported. Since distutils2/packaging
aims to maintain backwards compability, these commands should work on projects
that are packaged with distutils2/packaging as well as with other libraries
such as distutils, setuptools, and distribute.

Install
-------

Install one or more projects.

Usage: ``pip2 install <project>...``

Projects can be installed from the `Python Packaging Index (PyPI)`_::

    $ pip2 install TowelStuff sample-distutils2-project
    Successfully installed TowelStuff, sample-distutils2-project.

.. _Python Packaging Index (PyPI): http://pypi.python.org/pypi

Projects can also be installed from local archives (.zip, .tar.gz, .tar.bz2,
.tgz, or .tar) or directories::

    $ pip2 install sample-distutils2-project.tar.gz
    Successfully installed sample-distutils2-project.tar.gz

    $ pip2 install /path/to/TowelStuff
    Successfully installed /path/to/TowelStuff.

Freeze
------

Display a list of installed projects with their version.

Usage: ``pip2 freeze``

Example::

    $ pip2 freeze
    TowelStuff==0.1.1
    sample-distutils2-project==1.1.0


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

    $ pip2 uninstall sample-distutils2-project
    Successfully uninstalled sample-distutils2-project.
