import pip2.commands.install
import pip2.commands.freeze
import pip2.commands.search
import pip2.util

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
    dist_names = list(distributions.keys())
    dist_names.sort()
    for dist_name in dist_names:
        print(dist_name + "==" + distributions[dist_name]['version'])
        
    return

def search(args):
    results = pip2.commands.search.search(args.package)
    
    if results == {}:
        print("No search results found")
        return
        
    terminal_width = pip2.util.getTerminalSize()[0]
    
    name_len = 26 #package name alotted this many characters
    # package summary alotted this many characters per line, - 4 is for the ' - ' and 
    # leaving one extra space at end
    sum_len = terminal_width - name_len - 4 # 50
    
    #for each search result
    for res_key in results.keys():
        # how much of the summary we have printed
        printed = 0
        #get as much as can fit on the first line
        summary = results[res_key]['summary'][:sum_len]
        result = "{0:<{2}} - {1}".format(res_key[:name_len], summary, name_len)
        print(result)
        printed += sum_len
        # while we haven't printed all of the summary
        while(printed) < (len(results[res_key]['summary'])):
            # +3 is to compensate for ' - '
            result = " "*(name_len+3) + results[res_key]['summary'][printed:(printed+sum_len)]
            print(result)
            printed += sum_len
        #if the user already has the package installed print their installed version
        #and the latest version found on the index
        if ('installed_version' in results[res_key] and 'latest_version' in results[res_key]):
            print("   INSTALLED: {0}\n   LATEST   : {1}".format(results[res_key]['installed_version'], 
                                                                results[res_key]['latest_version']))
    return
    
    
    
