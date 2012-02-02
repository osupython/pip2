"""
__init__.py - Routes commands and arguments to the correct module
"""

from pip2.commands import _install, _uninstall, _search, _freeze, _bundle

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
    
def bundle(args):
    """
    Packages up a project and uploads it to PyPi
    """
    _bundle.run(args)
