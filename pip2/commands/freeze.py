"""The freeze command.

This module implements the freeze command with an interface that matches the
command line usage.

"""

from pip2.compat import packaging
from pip2.log import logger


def freeze():
    """Get a list of installed projects.

    Returns a dictionary where the keys are project names and the values are
    dictionaries with the following keys and values:

    * `'version'` - a string containing the project's version.

    For example, the return value may look like this::

        {   'TowelStuff': {'version': '0.1.1'},
            'pip2': {'version': '1.0'}}

    :rtype: dictionary

    """
    try:
        results = list(packaging.database.get_distributions(use_egg_info=True))
    except Exception as e:
        logger.exception(e)
        raise
    installed = dict()
    for dist in results:
        installed[dist.name] = dict()
        installed[dist.name]['version'] = str(dist.version)

    return installed
