"""
Returns a dictionary containing all installed packages.

return: A dictionary, key is package name value is a dictionary with
        information about package.
"""

import packaging.database


def freeze():
    results = list(packaging.database.get_distributions())
    installed = dict()
    for dist in results:
        installed[dist.name] = dict()
        installed[dist.name]['version'] = dist.version

    return installed
