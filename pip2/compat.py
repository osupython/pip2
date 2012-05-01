"""Stuff that differs in different Python versions."""

import sys


if sys.version_info >= (3, 3):
    import packaging
    import packaging.database
    import packaging.install
    import packaging.pypi
    try:
        import unittest.mock as mock
    except ImportError:
        # Mock isn't needed for normal functionality, so don't worry if it
        # can't be imported here; the tests will complain if they need it
        pass
else:
    import distutils2 as packaging
    import distutils2.database
    import distutils2.install
    import distutils2.pypi
    try:
        import mock
    except ImportError:
        # Mock isn't needed for normal functionality, so don't worry if it
        # can't be imported here; the tests will complain if they need it
        pass
