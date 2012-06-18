"""The install command.

This module implements the install command with an interface that matches the
command line usage.

"""

import os

from pip2.compat import packaging
from pip2.log import logger


def install(project_list):
    """Install a list of projects.

    Note that project dependencies are not yet detected and installed.

    Returns a dictionary with the following keys and values:

    * `'installed'` - a list of strings containing the projects that were
      successfully installed.

    * `'failed'` - a list of strings containing the projects that failed to
      install.

    :param project_list: the projects to install.  May be names of projects on
                         the Python Package Index (PyPI) or paths to local
                         directories and archives (.zip, .tar.gz, .tar.bz2,
                         .tgz, or .tar).
    :type project_list: iterable of strings
    :rtype: dictionary

    """
    result = {'installed': [], 'failed': []}

    for project in project_list:
        success = False

        try:
            if os.path.exists(project):
                success = packaging.install.install_local_project(project)
            else:
                success = packaging.install.install(project)
        except Exception as e:
            logger.exception(e)
            raise

        if success:
            result['installed'].append(project)
        else:
            result['failed'].append(project)

    return result
