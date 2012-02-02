"""
TODO: DOCSTRING
"""

import distutils2.database as packaging
import os.path

def run(args):
    """
    Prints a list of all currently installed distributions. Checks the args
    variable for display options.
    """
    print("Recieved {0}".format(args))
    
    try:
        distributions = packaging.get_distributions()
    except Exception as e:
        print("Unknown Exception Raised: {0}".format(e))
        return False #failure

    print("---------- Installed Packages ----------\n")
    
    #display distribution name, version, and directory
    i = 0
    if args.long:
        for dis in distributions:
            i += 1
            print("Name:       {0}\n".format(dis.name) + 
                  "Version:    {0}\n".format(dis.version) + 
                  "Dependency: {0}\n".format(dis.requested) +
                  "Location:   {0}\n".format(os.path.dirname(dis.path)))
    #just display the name
    else:
        for dis in distributions:
            i += 1
            print(dis.name)
        print("")
    
    print("Found {0} installed packages".format(i))
    return True #it worked
