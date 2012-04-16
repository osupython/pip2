"""
TODO: DOCSTRING
"""

import packaging.database


def freeze():
    results = list(packaging.database.get_distributions())
    installed = dict()
    for dist in results:
        installed[dist.name] = dict()
        installed[dist.name]['version'] = dist.version

    return installed
