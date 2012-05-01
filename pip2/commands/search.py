"""
Searches the PYPIs for packages based off of
the 'package' parameter, the default is the http://python.org/pypi index

package: search query (usually package name) as string.

return: A dictionary of search results. Key is package name value is dictionary
        containing information about the package.
"""

import logging

import pip2.commands.freeze
from pip2.compat import packaging


pkg_logger = logging.getLogger("packaging")
old_lvl = pkg_logger.getEffectiveLevel()


def search(package):
    """
    Searches the PYPIs for packages based off of
    the 'package' parameter, the default is the http://python.org/pypi index
    """
    results = dict()

    # temp for future ref, fail gracefully
    try:
        client = packaging.pypi.xmlrpc.Client()
    except:
        raise

    # don't display irrational version warnings
    pkg_logger.setLevel(logging.ERROR)
    # temp for future ref
    try:
        projects = client.search_projects(name=package, summary=package)
    except:
        raise
    finally:
        pkg_logger.setLevel(old_lvl)
    installed = pip2.commands.freeze.freeze()

    for project in projects:
        results[project.name] = dict()
        # temp for future ref.
        # Sometimes a release can't be found or
        # version number can't be rationalized
        try:
            # get the latest release
            project.sort_releases()
            release = project.releases[0]
        except IndexError:
            results[project.name]['summary'] = "CANNOT GET SUMMARY"
        else:
            results[project.name]['summary'] = release.metadata['summary']
            f = results[project.name]['summary']
            f = f.replace('\n', ' ').replace('\t', ' ').replace('  ', ' ')
            results[project.name]['summary'] = f
            if project.name in installed.keys():
                results[project.name]['installed_version'] = \
                installed[project.name]['version']
                results[project.name]['latest_version'] = release.version

    return results
