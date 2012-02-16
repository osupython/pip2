import distutils2.database 

def freeze():
    result = distutils2.database.get_distributions()
    
    #replace the iterator of distributions with just their name as a list
    return [distribution.name for distribution in result]
    

