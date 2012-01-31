"""
Search command built on top of the distutils.pypi.simple crawler
"""

#search returns a ReleasesList which is a list of ReleaseInfo's
from distutils2.pypi.dist import ReleasesList, ReleaseInfo
from distutils2.pypi.simple import Crawler
from distutils2.pypi.errors import ProjectNotFound, ReleaseNotFound
from distutils2.errors import IrrationalVersionError


def run(args):
    """
    Search indexes for packages that match args.package_name and display the results.
    An index can be specified using -i or --index-url followed by an address.
    You can specify -v or --version followed by a specific version number and
    search will return the closest match.
    
    In the future it will be changed to an expression so instead of returning a single
    match, it will return multiple and you can use an expression like >0.6.3,!=0.8.3,<=1.0.2
    to get all versions greater then 0.6.3 not 0.8.3 and all less then or equal to 1.0.2
    """
    
    #no index specified, use standard
    if not args.index_url:
        crawler = Crawler()
    #use custom index
    else:
        if isinstance(args.index_url, str):
            crawler = Crawler(index_url = args.index_url)
        else:
            print('--index-url must be a string')
            return False #failure
     
    print("Recieved {0}".format(args))
    
    print("\nSearching...\n")
    #search!
    if not args.version:
        return search_default(crawler, args)
    else:
        return search_version(crawler, args)
        

def search_default(crawler, args): 
        try:
            releaseList = crawler.get_releases(args.package_name)
        except ProjectNotFound:
            print("\nThe specified package could not be found. Please verify that the package name is correct," + \
                  " the Search command is case sensitive.\nPackage query: {0}".format(args.package_name))
            return False #failure
        except Exception as e:
            print("Unknown Exception raised: {0}".format(e))
            return False #failure
        
        #no exceptions were raised
        else:
            releaseList.sort_releases(reverse = False)
        
        #display the results!
        print("---------- Search Results ----------")
        for release in releaseList:
            print('\nName   : {0}'.format(release.name))
            print('Version: {0}'.format(release.version))
            dists = release.fetch_distributions()
            print('Dists  : ')
            i = 0
            #print all distributions for one release
            for key in dists.keys():
                i += 1
                print('{0}. {1}'.format(i, key))
        print("\nSearch found {0} results".format(len(releaseList)))
        return True #it worked
        

#use specified version expression 
def search_version(crawler, args):
        query = args.package_name + ' == ' + args.version
        try:
            release = crawler.get_release(query)
        except ProjectNotFound or ReleaseNotFound:
            print("\nThe specified package could not be found. Please verify that the package name and version" +\
                  " are correct, the Search command is case sensitive.\nPackage query: {0}".format(query))
            return False #failure
        except IrrationalVersionError:
            print("The specified version does not conform to any known standards. Version expressions should "+\
                  "follow the standards located in PEP345\nVersion Expression: {0}".format(args.version))
            return False #failure
        except ValueError as e:
            print("Value Error: {0}".format(e))
            return False #failure
        except Exception as e:
            print("Unknown exception raised: {0}".format(e))
            return False #failure
        
        print("---------- Search Results ----------")
        print('\nName   : {0}'.format(release.name))
        print('Version: {0}'.format(release.version))
        dists = release.fetch_distributions()
        print('Dists  : ')
        i = 0
        #print all distributions for one release
        for key in dists.keys():
            i += 1
            print('{0}. {1}'.format(i, key))
        return True #it worked

        
    
