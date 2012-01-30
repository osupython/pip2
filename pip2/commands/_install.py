"""
Install command implemented on top of distutils2.install.install()
"""

import distutils2.install

def run(args):
    """
    Checks argument 'args' for various install flags (such as --editable) and installs
    'args.package_name' using distutils2 library.
    """

    if args.editable:
        success = install_editable(args)
    else:
        success = install_default(args)

    if success:
        print("Successfully installed: {0}".format(args.package_name))
    else:
        print("Failed to install: {0}".format(args.package_name)) 

def install_editable(args):
    try:
        success = distutils2.install.install_local_project(args.package_name)
    except:
        success = False

    return success

def install_default(args):
    try:
        success = distutils2.install.install(args.package_name)
    except:
        success = False

    return success
    
