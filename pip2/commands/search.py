"""The search command.

This module implements the search command with an interface that matches the
command line usage.

"""

import pip2.commands.freeze
from pip2.compat import packaging


def search(query):
    """Search projects on the Python Package Index (PyPI).

    Searches the `name` and `summary` fields for projects that match `query`.

    Returns a dictionary containing the search results.  The keys are project
    names and the values are dictionaries with the following keys and values:

    * `'summary'` - a string containing the project's summary.

    * `'installed_version'` (only present if the project is installed) - a
      string containing the version of the project currently installed.

    * `'latest_version'` (only present if the project is installed) - a string
      containing the latest version of the project available on the index.

    For example, the return value may look like this::

        {   'TowelStuff': {   'installed_version': '0.1.1',
                              'latest_version': '0.1.1',
                              'summary': 'Useful towel-related stuff.'},
            'towel': {'summary': 'Keeping you DRY since 2010'}}

    :param query: the search query.
    :type query: string
    :rtype: dictionary

    """
    results = dict()
    client = packaging.pypi.xmlrpc.Client()
    projects = client.search_projects(name=query, summary=query)
    installed = pip2.commands.freeze.freeze()

    for project in projects:
        results[project.name] = dict()
        # if all releases for a project have irrational versions then the
        # releases list will be empty
        if project.releases:
            project.sort_releases()
            release = project.releases[0]
            results[project.name]['summary'] = release.metadata['summary']
            if project.name in installed.keys():
                results[project.name]['installed_version'] = \
                installed[project.name]['version']
                results[project.name]['latest_version'] = str(release.version)
        else:
            results[project.name]['summary'] = "CANNOT GET SUMMARY"

    return results
