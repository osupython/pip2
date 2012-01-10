"""
TODO: DOCSTRING
"""

import distutils2.install

def run(args):
    """
    TODO: DOCSTRING
    """
    print("Received {0}".format(args))

    if args.editable:
        install_editable()

    #distutils2.install.install(args.package_name)
