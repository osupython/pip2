import mock
import pip2.commands.search
import distutils2.pypi.xmlrpc

@mock.patch.object(distutils2.pypi.xmlrpc, 'Client')
class TestSearchAPI():
    
    def test_return_correct_results(self, mock_func):
        return False

@mock.patch.object(pip2.commands.search, 'search')    
class TestSearchCLI():
    
    def test_print_correct_results(self, mock_func):
        return False
    