====================
Contributing to Pip2
====================


Contributing with Code
======================

Supported Python Versions
-------------------------

Pip2 only supports Python 3.2 at the moment, but there are plans to support
versions of Python back to 2.6 (ish?).

Prerequisites
-------------

The following tools are required:

- Git
- Mercurial (``hg``)
- Python 3.2
- pip and virtualenv

You must also have a Github account and basic familiarity with the tools listed
above.

These instructions assume a Unix-like operating system (e.g., Mac or Linux).
Minor modifications may be required for contributing to pip2 on Windows.

Forking the Repository
----------------------

`Fork`_ the `main pip2 repository on Github`_, and then clone your personal
fork::

    $ git clone https://github.com/<YOUR_USER_NAME>/pip2

.. _Fork: http://help.github.com/fork-a-repo/
.. _main pip2 repository on Github: https://github.com/osupython/pip2

Installation
------------

Create and activate a virtualenv for pip2 development with Python 3.2::

    $ virtualenv --python=python3.2 pip2-dev-py3.2
    $ source pip2-dev-py3.2/bin/activate

Pip2 depends on distutils2, which doesn't have a recent version on PyPI. To
install the python3 branch of distutils2 from source::

    $ hg clone --branch python3 http://hg.python.org/distutils2
    $ pip install -e distutils2/


Install pip2::

    $ cd pip2/
    $ python setup.py develop

Running the Tests
-----------------

TODO


Contributing with Documentation
===============================

Building the Documentation
--------------------------

Install the tools required to build the documentation::

    $ pip install sphinx

Build the HTML version of the documentation::

    $ cd pip2/docs/
    $ make html

Launch ``pip2/docs/_build/html/index.html`` in your browser.
