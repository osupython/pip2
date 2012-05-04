Install
=======

Install one or more packages from PyPi (ignoring dependencies).

Usage: ``pip2 install <package>...``

Example::

    $ pip2 install package1
    Successfully installed package1
    $ pip2 install package2 package3
    Successfully installed package2 package3
    $ pip2 install package_that_doesnt_exist_or_fails_to_install
    Failed to install package_that_doesnt_exist_or_fails_to_install
    $ pip2 install a-real-package not-a-package
    Successfully installed a-real-package.
    Failed to install not-a-package.


Freeze
======

Display a list of currently-installed packages.

Usage: ``pip2 freeze``

Example::

    $ pip2 freeze
    $ # ...Install a few packages...
    $ pip2 freeze
    package1==1.0
    package2==1.5
    package3==2.0


Search
======

Search PyPi.

Usage: ``pip2 search <query>``

Example::

    $ pip2 search query_with_no_results
    Search returned no results...
    $ pip2 search pyglet
    simplui                    - Light-weight GUI toolkit for pyglet
    svgbatch                   - Loads SVG files into pyglet Batch objects for Open
                                 GL rendering.
    Fungus                     - A simple scene based game engine building on pygle
                                 t.
    snowui                     - snowui is a fast and simple GUI using pyglet and r
                                 abbyt.
    pygarrayimage              - Allow numpy arrays as source of texture data for p
                                 yglet.
    gloopy                     - Gloopy is a Python library for creating 3D polyhed
                                 ra and rendering them using OpenGL. It uses Pyglet
                                 to open a window and manage events, and PyOpenGL
                                 for OpenGL bindings.
    pyglet                     - Cross-platform windowing and multimedia library
    kytten                     - GUI Framework for Pyglet


Uninstall
=========

Uninstall one or more packages.

Usage: ``pip2 uninstall <package>...``

Example::

    $ pip2 uninstall package
    Successfully uninstalled package1
    $ pip2 uninstall package2 package3
    Successfully uninstalled package2 package3
    $ pip2 uninstall package_that_isnt_installed_or_failed_to_uninstall
    Failed to uninstall package_that_isnt_installed_or_failed_to_uninstall

