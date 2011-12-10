"""
TODO: DOCSTRING
"""

import distutils2.install

def run(args):
    """
    TODO: DOCSTRING
    """
    print("Recieved {0}".format(args))
    distutils2.install.remove(args.package_name)
