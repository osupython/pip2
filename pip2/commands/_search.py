"""
Search command built on top of the distutils.pypi.simple crawler
"""

def run(args):
    """
    Search indexes for packages that match args.package_name and display the results.
    An index can be specified using -i or --index-url followed by an address.
    """
    
    #search returns a ReleasesList which is a list of ReleaseInfo's
    from distutils2.pypi.dist import ReleasesList, ReleaseInfo
    from distutils2.pypi.simple import Crawler
    
    #no index specified, use standard
    if not args.index_url:
        crawler = Crawler()
    #use custom index
    else:
        if isinstance(args.index_url, str):
            crawler = Crawler(index_url = args.index_url)
        else:
            print('--index-url must be a string')
            return
    
    print("Recieved {0}".format(args))
    
    #search!
    releaseList = crawler.get_releases(args.package_name)
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
        
    
