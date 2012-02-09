import distutils2.database as packaging

get_distributions = packaging.get_distributions

def freeze():
    result = get_distributions()
    return list(result)

