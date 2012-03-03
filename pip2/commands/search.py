from distutils2.pypi import xmlrpc
import pip2.commands.freeze

def search(package):
    """
    Searches the PYPIs for packages based off of
    the 'package' parameter, the default is the http://python.org/pypi index
    """

    #dictionary to hold results. Key is package name, value is dict with summary and match info
    results = dict()

    #create the client to connect to package indexes
    try: #temp for future ref, fail gracefully
        client = xmlrpc.Client()
    except:
        raise
    
    #get installed packages for comparisons against search results (will also need version numbers eventually)
    installed = pip2.commands.freeze.freeze(version = True)
    
    # convert all keys to lowercase for easy matching
    installed_low = dict()
    for dist_name in installed.keys():
        installed_low[dist_name.lower()] = installed[dist_name]
        
    #search_projects returns a list of projects
    try: #temp for future ref
        projects = client.search_projects(name = package)
    except:
        raise

    #for each project, which is really just a releasesList 
    for project in projects:
        #print(project)
        #gets the latest release
        try: #temp for future ref. Sometimes a release can't be found or version number can't be rationalized
            release = project.releases[0]
        except:
            raise
        
        results[project.name] = {}
        results[project.name]['summary'] = release.metadata['summary']
        
        #if this package from search results is already installed then keep track of it
        if project.name.lower() in installed_low.keys():
            results[project.name]['installed_version'] = installed_low[project.name.lower()]['version']
            results[project.name]['latest_version'] = release.version
        
    return results


        

