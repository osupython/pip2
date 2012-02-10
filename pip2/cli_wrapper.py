import pip2.commands.install
import pip2.commands.freeze
import sys

def install(args):
    result = pip2.commands.install.install(args.package_list)

    if result['installed'] != []:
        successful = " ".join(map(str, result['installed']))
        print("Successfully installed {0}.".format(successful))
    if result['failed'] != []:
        failed = " ".join(map(str, result['failed']))
        print("Failed to install {0}.".format(failed))

    return

def freeze(args):
    distributions = pip2.commands.freeze.freeze()
    
    for dis in distributions:
        print(dis)
    return
    
    
