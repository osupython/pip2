import distutils2.install

def install(package_list):
    result = {'installed':[], 'failed':[]}

    for package in package_list:
        if distutils2.install.install(package):
            result['installed'].append(package)
        else:
            result['failed'].append(package)

    return result
