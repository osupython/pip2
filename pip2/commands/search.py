from distutils2.pypi import wrapper
import pip2.commands.freeze

def search(package):
    """
    Searches the PYPIs for packages based off of
    the 'package' parameter, the default is the http://python.org/pypi index
    """
    
    #dictionary to hold results. Key is package name, value is summary of package
    results = dict()
    #dictionary which holds the matches from search results and already installed packages
    #each value is also a dictionary with keys 'installed' and 'latest'
    matches = dict()
    #create the client to connect to package indexes
    client = wrapper.ClientWrapper(default_index = 'xmlrpc')
    
    #get installed packages for comparisons against search results (will also need version numbers eventually)
    installed = pip2.commands.freeze.freeze()
    
    #search_projects returns a list of releasesLists
    packages = client.search_projects(name = package)
    print(packages)
    
    #for each package 
    for pkg in packages:
        #get the latest release (based off latest version)
        print('\n{0}\n{1}\n'.format(pkg, dir(pkg)))
        pk = client.get_releases(pkg)
        print(pk.fetch_releases())
        
        #add the summary of the project, which is located in the release's metadata
        results[pkg['name']] = release.metadata.get('summary')
        #is one of the installed packages showing up in search results?
        if pkg['name'] in installed:
            #'installed' will be retrieved through the freeze command, 1.0 is a place holder
            #'latest' is retrieved from the latest release's version
            matches[pkg['name']] = {'installed':1.0, 'latest':release.version}
    
    return results, matches

