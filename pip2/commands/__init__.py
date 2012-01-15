"""
__init__.py - Routes commands and arguments to the correct module
"""

from pip2.commands import _install, _uninstall, _search, _freeze

def install(args):
    """
    Installs a packages.
    """
    _install.run(args)

def uninstall(args):
    """
    Uninstalls a package.
    """
    _uninstall.run(args)

def search(args):
    """
    Searchs PyPI (or another index) for a package.
    """
    _search.run(args)

def freeze(args):
    """
    Lists installed packages.
    """
    _freeze.run(args)
