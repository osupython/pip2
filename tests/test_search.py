import mock
import pip2.commands.search
import distutils2.pypi.xmlrpc
import pip2.commands.freeze

@mock.patch.object(pip2.commands.freeze, 'freeze')
@mock.patch.object(distutils2.pypi.xmlrpc.Client, 'search_projects')
class TestSearchAPI():
    
    def test_basic_search(self, mock_search_projects, mock_freeze):
        
        test_proj1 = mock.Mock()
        test_proj1.name = 'test_proj1'
        test_proj1.releases = mock.MagicMock()
        test_proj1.releases[0].version = 1.5
        test_proj1.releases[0].metadata = {}
        test_proj1.releases[0].metadata['summary'] = 'Summary for project 1'
        
        test_proj2 = mock.Mock()
        test_proj2.name = 'test_proj2'
        test_proj2.releases = mock.MagicMock()
        test_proj2.releases[0].version = 2.5
        test_proj2.releases[0].metadata = {}
        test_proj2.releases[0].metadata['summary'] = 'Summary for project 2'
        
        test_proj3 = mock.Mock()
        test_proj3.name = 'test_proj3'
        test_proj3.releases = mock.MagicMock()
        test_proj3.releases[0].version = 3.5
        test_proj3.releases[0].metadata = {}
        test_proj3.releases[0].metadata['summary'] = 'Summary for project 3'
        
        mock_search_projects.return_value = [test_proj1, test_proj2, test_proj3]
        mock_freeze.return_value = {'test_proj1':{'version':1.0}, 'test_proj3':{'version':3.0}}
        
        expected = {'test_proj1':{'summary':'Summary for project 1', 
                                  'installed_version':1.0, 'latest_version':1.5}, 
                    'test_proj2':{'summary':'Summary for project 2'}, 
                    'test_proj3':{'summary':'Summary for project 3', 
                                  'installed_version':3.0, 'latest_version':3.5}}
        
        result = pip2.commands.search.search('test')
        
        #compare the two
        try:
            assert result == expected
        #not the same? print out both lists
        except AssertionError:
            print('result  : {0}'.format(result))
            print('expected: {0}'.format(expected))
            raise
        

@mock.patch.object(pip2.commands.search, 'search')    
class TestSearchCLI():
    
    def test_basic_search(self, mock_func):
        return False
    