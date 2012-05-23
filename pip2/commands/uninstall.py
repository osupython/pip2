"""The uninstall command.

This module implements the uninstall command with an interface that matches the
command line usage.

"""

from pip2.compat import packaging


def uninstall(project_list):
    """Uninstall a list of projects.

    Returns a dictionary with the following keys and values:

    * `'uninstalled'` - a list of strings containing the names of the projects
      that were successfully uninstalled.

    * `'failed'` - a list of strings containing the names of the projects that
      failed to uninstall.

    :param project_list: the names of the projects to uninstall.
    :type project_list: iterable of strings
    :rtype: dictionary

    """
    result = {'uninstalled': [], 'failed': []}

    for project in project_list:
        if packaging.install.remove(project):
            result['uninstalled'].append(project)
        else:
            result['failed'].append(project)

    return result
