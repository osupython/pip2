"""
TODO: DOCSTRING
"""

import distutils2.database

def run(args):
    """
    Prints a list of all currently installed distributions. Checks the args
    variable for display options.
    """
    print("Recieved {0}".format(args))
    
    distributions = distutils2.database.get_distributions()
    
    print("---------- Installed Packages ----------\n")
    
    #display distribution name and version
    if args.long:
        for dis in distributions:
            print("{:<25}".format(dis.name) + "{:>15}".format(dis.version))
    #just display the name
    else:
        for dis in distributions:
            print(dis.name)
