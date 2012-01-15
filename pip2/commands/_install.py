"""
Install command implemented on top of distutils2.install.install()
"""

import distutils2.install

def run(args):
    """
    Checks argument 'args' for various install flags (such as --editable) and installs
    'args.package_name' using distutils2 library.
    """
    distutils2.install.install(args.package_name)
