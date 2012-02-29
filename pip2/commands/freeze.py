import distutils2.database 

def freeze():
    result = distutils2.database.get_distributions()
    
    #replace the iterator of distributions with just a list of names
    return [distribution.name for distribution in result]
    

