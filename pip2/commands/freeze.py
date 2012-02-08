import distutils2.database as packaging

get_distributions = packaging.get_distributions

def freeze():
    result = command()
    return list(result)

