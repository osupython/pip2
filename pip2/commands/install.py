"""
Installs a package and returns a dictionary containing which packages
were installed successfully or unsuccessfully.
"""

import packaging.install
import os


def install(package_list):
    result = {'installed': [], 'failed': []}

    for package in package_list:
        success = False

        if os.path.exists(package):
            success = packaging.install.install_local_project(package)
        else:
            success = packaging.install.install(package)

        if success:
            result['installed'].append(package)
        else:
            result['failed'].append(package)

    return result
