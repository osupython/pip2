"""
Installs a package and returns a dictionary containing which packages
were installed successfully or unsuccessfully.
"""

import packaging.install

# TODO: Install dependencies automatically
def install(package_list):
    result = {'installed': [], 'failed': []}

    for package in package_list:
        if packaging.install.install(package):
            result['installed'].append(package)
        else:
            result['failed'].append(package)

    return result
