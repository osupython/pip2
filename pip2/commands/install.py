"""
TODO: DOCSTRING
"""

import packaging.install


def install(package_list):
    result = {'installed': [], 'failed': []}

    for package in package_list:
        if packaging.install.install(package):
            result['installed'].append(package)
        else:
            result['failed'].append(package)

    return result
