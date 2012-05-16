"""
Searches the PYPIs for packages based off of
the 'package' parameter, the default is the http://python.org/pypi index

package: search query (usually package name) as string.

return: A dictionary of search results. Key is package name value is dictionary
        containing information about the package.
"""

import pip2.commands.freeze
from pip2.compat import packaging


def search(package):
    """
    Searches the PYPIs for packages based off of
    the 'package' parameter, the default is the http://python.org/pypi index
    """
    results = dict()
    client = packaging.pypi.xmlrpc.Client()
    projects = client.search_projects(name=package, summary=package)
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
                results[project.name]['latest_version'] = release.version
        else:
            results[project.name]['summary'] = "CANNOT GET SUMMARY"

    return results
