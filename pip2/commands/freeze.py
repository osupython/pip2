import distutils2.database 

def freeze(version = False):
    # dictionary to hold info about installed dists.
    # key is dist's name, value is a dictionary to hold info populated by
    # freeze's various options
    installed = dict()
    results = list(distutils2.database.get_distributions())
    
    for dist in results:
        installed[dist.name] = dict()
        
        # if the version option (-v) has been specified 
        if version:
            installed = _version(dist, installed)
        
    return installed


def _version(dist, installed):
    # populate version info for the dist
    installed[dist.name]['version'] = dist.version
            
    return installed
    

