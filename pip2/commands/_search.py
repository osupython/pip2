"""
Search command built on top of the distutils.pypi.simple crawler
"""

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
    
    print("---------- Search Results ----------")
    #search!
    if not args.version:
        releaseList = crawler.get_releases(args.package_name)
        releaseList.sort_releases(reverse = False)
        
        #display the results!
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
        
    #use specified version expression 
    else:
        query = args.package_name + ' ==' + args.version
        release = crawler.get_release(query)
        
        print('\nName   : {0}'.format(release.name))
        print('Version: {0}'.format(release.version))
        dists = release.fetch_distributions()
        print('Dists  : ')
        i = 0
        #print all distributions for one release
        for key in dists.keys():
            i += 1
            print('{0}. {1}'.format(i, key))

        
    
