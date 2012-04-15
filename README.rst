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


Freeze
======

Display a list of currently-installed packages.

Usage: ``pip2 freeze``

Example::

    $ pip2 freeze
    $ # ...Install a few packages...
    $ pip2 freeze
    package1
    package2
    package3


Search
======

Search PyPi.

Usage: ``pip2 search <query>``

Example::

    $ pip2 search query_with_no_results
    $ pip2 search pypy
    JitViewer
    pypyenv
    tkinter-pypy
    pypq
    eolfixer
    hackbeil


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
