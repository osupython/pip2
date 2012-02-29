from distutils2.pypi import xmlrpc
import pip2.commands.freeze

def search(package):
    """
    Searches the PYPIs for packages based off of
    the 'package' parameter, the default is the http://python.org/pypi index
    """

    #dictionary to hold results. Key is package name, value is summary of package
    results = dict()
    #dictionary to hold matches of search results and installed packages
    #key is package name and value is dictionary with installed version and queried version
    matches = dict()

    #create the client to connect to package indexes
    try: #temp for future ref, fail gracefully
        client = xmlrpc.Client()
    except:
        raise
    
    #get installed packages for comparisons against search results (will also need version numbers eventually)
    installed = [dis.lower() for dis in pip2.commands.freeze.freeze()]
    #search_projects returns a list of projects
    try: #temp for future ref
        projects = client.search_projects(name = package)
    except:
        raise
    
    #for each project, which is really just a releasesList 
    for project in projects:
        #gets the latest release
        try: #temp for future ref. Sometimes a release can't be found or version number can't be rationalized
            release = project.releases[0]
        except:
            raise
        
        results[project.name] = release.metadata['summary']
        #if this package from search results is already installed then keep track of it
        if project.name.lower() in installed:
            matches[project.name.lower()] = {'installed':1.0, 'latest':release.version}
        
    return results, matches


        

