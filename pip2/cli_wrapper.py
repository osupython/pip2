import pip2.commands.install
import pip2.commands.freeze
import pip2.commands.search
import sys, os

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
    terminal_width = 80 #get actual terminal width somehow?
    name_len = 26 #package name alotted this many characters
    # package summary alotted this many characters per line, - 4 is for the ' - ' and 
    # leaving one extra space at end
    sum_len = terminal_width - name_len - 4 # 50
    
    #for each search result
    for res_key in results.keys():
        # how much of the summary we have printed
        printed = 0
        #get as much as can fit on the first line
        summary = results[res_key][:sum_len]
        result = "{0:<{2}} - {1}".format(res_key[:name_len], summary, name_len)
        print(result)
        printed += sum_len
        # while we haven't printed all of the summary
        while(printed) < (len(results[res_key])):
            # +3 is to compensate for ' - '
            result = " "*(name_len+3) + results[res_key][printed:(printed+sum_len)]
            print(result)
            printed += sum_len
        #if the user already has the package installed print their installed version
        #and the latest version found on the index
        if res_key.lower() in matches.keys():
            print("   INSTALLED: {0}\n   LATEST   : {1}".format(matches[res_key.lower()]['installed'], 
                                                                matches[res_key.lower()]['latest']))
    return
    
    
    
