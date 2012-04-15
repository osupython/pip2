import packaging.database 

def freeze():
    # dictionary to hold info about installed dists.
    # key is dist's name, value is a dictionary to hold info populated by
    # freeze's various options
    installed = dict()
    results = list(packaging.database.get_distributions())
    
    for dist in results:
        installed[dist.name] = dict()
        installed[dist.name]['version'] = dist.version
        
    return installed


