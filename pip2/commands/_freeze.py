"""
TODO: DOCSTRING
"""

import distutils2.database

def run(args):
    """
    TODO: DOCSTRING
    """
    print("Recieved {0}".format(args))
    
    distributions = distutils2.database.get_distributions()
    
    print("----- Installed Distributions -----\n")
    
    for dis in distributions:
        print(dis.name)
