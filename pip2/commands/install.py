import distutils2.install

func = distutils2.install.install

def install(package_list):
    result = {'installed':[], 'failed':[]}

    for package in package_list:
        if func(package):
            result['installed'].append(package)
        else:
            result['failed'].append(package)

    return result
