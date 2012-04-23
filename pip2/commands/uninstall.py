"""
TODO: DOCSTRING
"""

import packaging.install


def uninstall(package_list):
    result = {'uninstalled': [], 'failed': []}

    for package in package_list:
        if packaging.install.remove(package):
            result['uninstalled'].append(package)
        else:
            result['failed'].append(package)

    return result
