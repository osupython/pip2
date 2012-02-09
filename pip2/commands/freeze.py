import distutils2.database as packaging

get_distributions = packaging.get_distributions

def freeze():
    result = get_distributions()
    
    #replace the iterator of distributions with just their name as a list
    return [distribution.name for distribution in result]
    #return list(result)

