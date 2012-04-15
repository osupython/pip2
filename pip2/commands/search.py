import packaging.pypi.xmlrpc
import pip2.commands.freeze
import logging

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
        projects = client.search_projects(name = package)
    except:
        raise
    finally:
        pkg_logger.setLevel(old_lvl)
    installed = pip2.commands.freeze.freeze()
    
    for project in projects:
        results[project.name] = dict()
        # temp for future ref.
        # Sometimes a release can't be found or version number can't be rationalized
        try:  
            # get the latest release
            release = project.releases[0]
        except IndexError:
            results[project.name]['summary'] = "CANNOT GET SUMMARY"
        else:
            results[project.name]['summary'] = release.metadata['summary']
            if project.name in installed.keys():
                results[project.name]['installed_version'] = installed[project.name]['version']
                results[project.name]['latest_version'] = release.version
      
    return results


        

