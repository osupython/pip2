import distutils2.install

command = distutils2.install.remove

def uninstall(package=None):
    result = command(package)
    return result
