====================
Contributing to Pip2
====================


Contributing with Code
======================

Supported Python Versions
-------------------------

Pip2 currently only supports Python 3.2 and 3.3 (scheduled for release in
August 2012), but there are plans to support versions of Python back to
2.6-ish.

Prerequisites
-------------

The following tools are required:

- Python 3.2 or 3.3 (preferably both)
- Git
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

Create and activate a virtualenv for pip2 development. For example, if you are
developing with Python 3.2::

    $ virtualenv --python=python3.2 pip2-dev-py3.2
    $ source pip2-dev-py3.2/bin/activate

For versions of Python prior to 3.3, pip2 depends on distutils2 which is often
`broken`_ and/or outdated on PyPI. For now, just use pip to install from the
python3 branch of the distutils2 repository::

    $ pip install http://hg.python.org/distutils2/archive/python3.tar.bz2

.. _broken: http://github.com/osupython/pip2/issues/45

Install pip2::

    $ cd pip2/
    $ python setup.py develop

Running the Tests
-----------------

Pip2 uses `nose`_ and `mock`_ for testing. To install nose::

    $ pip install nose

Mock has been included in Python's standard library since version 3.3. For
versions of Python prior to 3.3::

    $ pip install mock

.. _nose: http://nose.readthedocs.org/
.. _mock: http://www.voidspace.org.uk/python/mock/

Now, run the unit tests from the root directory of the pip2 repository. You
should run these tests frequently as you are modifying the code::

    $ nosetests

If the `coverage`_ module is installed (`pip install coverage`), options may be
provided to nose so that coverage data is generated::

    $ nosetests --with-coverage

Usually only coverage data for pip2 will be needed. To run the coverage tool on
just the pip2 package::

    $ nosetests --with-coverage --cover-package=pip2

To generate HTML coverage data in the ./cover/ directory::

    $ nosetests --with-coverage --cover-package=pip2 --cover-html

Once your changes are working well in your development environment, `tox`_ can
be used to run these same tests in a clean environment under multiple versions
of Python. First, install tox::

    $ pip install tox

The first time you run it, tox will take a while (quite a few minutes) to build
virtualenvs and install the required packages::

    $ tox

Subsequent tox runs will reuse the existing virtualenvs and run much faster.
Note, however, that you may want to occasionally force the virtualenvs to be
recreated by running `tox --recreate` to get the latest versions of pip2's
dependencies. Run `tox --help`, visit `tox's website`_, or view the `tox.ini`
file in pip2's repository for additional information on using tox.

.. _coverage: http://nedbatchelder.com/code/coverage/
.. _tox: http://tox.readthedocs.org/
.. _tox's website: http://tox.readthedocs.org/


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
