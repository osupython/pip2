import pip2.commands.install
import pip2.commands.freeze
import pip2.commands.search
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

def search(args):
    results, matches = pip2.commands.search.search(args.package)
    
    #for each search result
    for res_key in results.keys():
        #print the package name and summary
        print("{0} - {1}".format(res_key, results[res_key]))
        #if the user already has the package installed print their installed version
        #and the latest version found on the index
        if res_key.lower() in matches.keys():
            print("INSTALLED: {0}\nLATEST   : {1}".format(matches[res_key.lower()]['installed'], 
                                                          matches[res_key.lower()]['latest']))
    return
    
    
    
