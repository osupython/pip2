import distutils2.install

command = distutils2.install.install

def install(package=None):
    result = command(package)
    return result

