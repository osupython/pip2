"""
Uninstalls a package and returns a dictionary containing which packages
were uninstalled successfully or unsuccessfully.
"""

from pip2.compat import packaging


def uninstall(package_list):
    result = {'uninstalled': [], 'failed': []}

    for package in package_list:
        if packaging.install.remove(package):
            result['uninstalled'].append(package)
        else:
            result['failed'].append(package)

    return result
