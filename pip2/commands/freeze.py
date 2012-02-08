import distutils2.database as packaging

command = packaging.get_distributions

def freeze():
    result = command()
    return list(result)

