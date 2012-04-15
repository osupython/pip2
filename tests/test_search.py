from io import StringIO
import inspect
import mock, sys
import pip2.commands.search
import packaging.pypi.xmlrpc
import pip2.commands.freeze

@mock.patch.object(pip2.commands.freeze, 'freeze')
@mock.patch.object(packaging.pypi.xmlrpc.Client, 'search_projects')
class TestSearchAPI():
    
    def setup(self):
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
        
        return [test_proj1, test_proj2, test_proj3]
    
    
    def test_basic_search(self, mock_search_projects, mock_freeze):
        mock_search_projects.return_value = self.setup()
        mock_freeze.return_value = {}
        
        expected = {'test_proj1':{'summary':'Summary for project 1'}, 
                    'test_proj2':{'summary':'Summary for project 2'}, 
                    'test_proj3':{'summary':'Summary for project 3'}}
        
        result = pip2.commands.search.search('test')
        
        self.tear_down(result, expected)


    def test_basic_search_matches(self, mock_search_projects, mock_freeze):
        mock_search_projects.return_value = self.setup()
        mock_freeze.return_value = {'test_proj1':{'version':1.0}, 'test_proj3':{'version':3.0}}
        
        expected = {'test_proj1':{'summary':'Summary for project 1', 
                                  'installed_version':1.0, 'latest_version':1.5}, 
                    'test_proj2':{'summary':'Summary for project 2'}, 
                    'test_proj3':{'summary':'Summary for project 3', 
                                  'installed_version':3.0, 'latest_version':3.5}}
        
        result = pip2.commands.search.search('test')
        
        self.tear_down(result, expected)
        
        
    def tear_down(self, result, expected):
        #compare the two
        try:
            assert result == expected
        #not the same? print out both lists
        except AssertionError:
            print('result  : {0}'.format(result))
            print('expected: {0}'.format(expected))
            raise


@mock.patch.object(pip2.util, 'getTerminalSize')
@mock.patch.object(pip2.commands.search, 'search')    
class TestSearchCLI():
    default_term_size = 80
    term_size = default_term_size
    name_len = 26
    cli_sep = ' - '
    buffer = len(cli_sep)
    sum_len = term_size - name_len - buffer - 1
    args = mock.Mock()
    args.package = "pkgPlaceholder"
    originalOut = sys.stdout
    
    def setup(self):
        sys.stdout = result = StringIO() 
        return result
    
    
    def test_basic_display_no_results(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.package = "nonexistantPackage"
        mock_getTerminalSize.return_value = (self.term_size, None)
        mock_search.return_value = {}
        
        expected = "No search results found\n"
        pip2.cli_wrapper.search(self.args)
        
        self.tear_down(result.getvalue(), expected)
        
    
    def test_basic_display_name_short(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.package = "shortPackage"
        mock_getTerminalSize.return_value = (self.term_size, None)
        mock_search.return_value = {self.args.package:{'summary':'summary placeholder'}}
        
        expected = self.args.package
        expected += (" "*(self.name_len - len(expected)) + self.cli_sep + 
                     "summary placeholder\n")
        pip2.cli_wrapper.search(self.args)
        
        self.tear_down(result.getvalue(), expected)
        
    
    def test_basic_display_name_long(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.package = "thisIsAVeryLongPackageThatCantDisplayFully"
        mock_getTerminalSize.return_value = (self.term_size, None)
        mock_search.return_value = {self.args.package:{'summary':'summary placeholder'}}
        
        expected = (self.args.package[:self.name_len] + self.cli_sep + 
                    "summary placeholder\n")
        pip2.cli_wrapper.search(self.args)
        
        self.tear_down(result.getvalue(), expected)
        
    
    def test_basic_display_desc_single_line(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.package = "pkgPlaceholder"
        mock_getTerminalSize.return_value = (self.term_size, None)
        desc = 'X'*(self.sum_len)
        mock_search.return_value = {self.args.package:{'summary':desc}}
        
        expected = (self.args.package + ' '*(self.name_len - len(self.args.package)) + 
                    self.cli_sep + desc + '\n')        
        pip2.cli_wrapper.search(self.args)
        
        self.tear_down(result.getvalue(), expected)
        
        
    def test_basic_display_desc_word_wrap(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.package = "pkgPlaceholder"
        mock_getTerminalSize.return_value = (self.term_size, None)
        desc = 'X'*int(self.sum_len*1.5)
        mock_search.return_value = {self.args.package:{'summary':desc}}
        
        desc_ln1 = desc[:self.sum_len]
        desc_ln2 = desc[len(desc_ln1):]
        expected = (self.args.package + ' '*(self.name_len - len(self.args.package)) + 
                    self.cli_sep + desc_ln1 + '\n' + 
                    ' '*(self.name_len + self.buffer) + desc_ln2 + '\n')
        
        pip2.cli_wrapper.search(self.args)
        
        self.tear_down(result.getvalue(), expected)
    
    
    def test_basic_display_matches(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.package = "pkgPlaceholder"
        mock_getTerminalSize.return_value = (self.term_size, None)
        
        assert 0
    
    def test_basic_display_small_terminal_size(self, mock_search, mock_getTerminalSize):
        self.term_size = 60
        self.sum_len = self.term_size - self.name_len - self.buffer - 1
        self._run_all_package_info_tests()
        self.term_size = self.default_term_size
        
        
    def test_basic_display_large_terminal_size(self, mock_search, mock_getTerminalSize):
        self.term_size = 180
        self.sum_len = self.term_size - self.name_len - self.buffer - 1
        self._run_all_package_info_tests()
        self.term_size = self.default_term_size
        
        
    def _run_all_package_info_tests(self):
        self.test_basic_display_no_results()        
        self.test_basic_display_name_short()
        self.test_basic_display_name_long()
        self.test_basic_display_desc_single_line()
        self.test_basic_display_desc_word_wrap()
    
    
    def tear_down(self, result, expected):
        #compare the two
        try:
            assert result == expected
        #not the same? print out both lists
        except AssertionError:
            result = result.replace('\n', '\\n')
            expected = expected.replace('\n', '\\n')
            
            if self.term_size == self.default_term_size:
                parent = "No Parent"
            else:
                parent = inspect.stack()[4][3]
                
            output = ("\n\nTEST FAILED" + 
                      "\nFunction  : {0}".format(inspect.stack()[1][3]) +
                      "\nParent    : {0}".format(parent) + 
                      "\nTerm width: {0}".format(self.term_size) + 
                      "\nResult    :\n{0}\n".format(result) + 
                      "\nExpected  :\n{0}".format(expected))
            
            print(output, file=sys.stderr)
            raise
        finally:
            sys.stdout = self.originalOut


    