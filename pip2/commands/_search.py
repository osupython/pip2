"""
TODO: DOCSTRING
"""

def run(args):
    """
    TODO: DOCSTRING
    """
    
    from distutils2.pypi.dist import ReleasesList, ReleaseInfo
    from distutils2.pypi.simple import Crawler
    
    crawler = Crawler()
    
    print("Recieved {0}".format(args))
    
    releaseList = crawler.get_releases(args.package_name)
    releaseList.sort_releases()
    
    print('\n')
    for release in releaseList:
        print('Name   : {0}'.format(release.name))
        print('Version: {0}'.format(release.version))
        dists = release.fetch_distributions()
        print('Dists  : ')
        i = 0
        for key in dists.keys():
            i += 1
            print('{0}. {1}'.format(i, key))
    
