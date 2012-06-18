import inspect
import sys
from io import StringIO

import pip2.commands.freeze
import pip2.commands.search
import tests.log
from pip2.compat import mock
from pip2.compat import packaging


@mock.patch.object(pip2.commands.freeze, 'freeze')
@mock.patch.object(packaging.pypi.xmlrpc.Client, 'search_projects')
class TestSearchAPI():
    def setup(self):
        test_proj1 = mock.Mock()
        test_proj1.name = 'test_proj1'
        test_proj1.releases = mock.MagicMock()
        test_proj1.releases[0].version = '1.5'
        test_proj1.releases[0].metadata = {}
        test_proj1.releases[0].metadata['summary'] = 'Summary for project 1'

        test_proj2 = mock.Mock()
        test_proj2.name = 'test_proj2'
        test_proj2.releases = mock.MagicMock()
        test_proj2.releases[0].version = '2.5'
        test_proj2.releases[0].metadata = {}
        test_proj2.releases[0].metadata['summary'] = 'Summary for project 2'

        test_proj3 = mock.Mock()
        test_proj3.name = 'test_proj3'
        test_proj3.releases = mock.MagicMock()
        test_proj3.releases[0].version = '3.5'
        test_proj3.releases[0].metadata = {}
        test_proj3.releases[0].metadata['summary'] = 'Summary for project 3'

        return [test_proj1, test_proj2, test_proj3]

    def test_basic_search(self, mock_search_projects, mock_freeze):
        mock_search_projects.return_value = self.setup()
        mock_freeze.return_value = {}

        expected = {'test_proj1': {'summary': 'Summary for project 1'},
                    'test_proj2': {'summary': 'Summary for project 2'},
                    'test_proj3': {'summary': 'Summary for project 3'}}

        result = pip2.commands.search.search('test')

        self.tear_down(result, expected)

    def test_basic_search_matches(self, mock_search_projects, mock_freeze):
        mock_search_projects.return_value = self.setup()
        mock_freeze.return_value = {'test_proj1': {'version': '1.0'},
                                    'test_proj3': {'version': '3.0'}}

        expected = {'test_proj1': {'summary': 'Summary for project 1',
                                   'installed_version': '1.0',
                                  'latest_version': '1.5'},
                    'test_proj2': {'summary': 'Summary for project 2'},
                    'test_proj3': {'summary': 'Summary for project 3',
                                   'installed_version': '3.0',
                                   'latest_version': '3.5'}}
        result = pip2.commands.search.search('test')

        self.tear_down(result, expected)

    def tear_down(self, result, expected):
        try:
            assert result == expected
        except AssertionError:
            print('result  : {0}'.format(result))
            print('expected: {0}'.format(expected))
            raise


@mock.patch.object(pip2.util, 'getTerminalSize')
@mock.patch.object(pip2.commands.search, 'search')
class TestSearchCLI():
    min_term_width = 40
    default_term_width = 80
    term_width = default_term_width
    name_len = 26
    sep = ' - '
    sep_len = len(sep)
    sum_len = term_width - name_len - sep_len - 1
    args = mock.Mock()
    args.project = 'pkgPlaceholder'

    def setup(self):
        result = tests.log.setup_logger()
        return result

    def test_basic_display_no_results(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.project = 'nonexistantproject'
        mock_getTerminalSize.return_value = (self.term_width, None)
        mock_search.return_value = {}
        expected = 'Search returned no results...\n'
        pip2.cli_wrapper.search(self.args)
        self.tear_down(result.getvalue(), expected)

    def test_basic_display_name_short(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.project = 'shortproject'
        mock_getTerminalSize.return_value = (self.term_width, None)
        mock_search.return_value = {self.args.project: {'summary': 'sum'}}
        expected = self.args.project
        expected += ' ' * (self.name_len - len(expected)) + self.sep + 'sum\n'
        pip2.cli_wrapper.search(self.args)
        self.tear_down(result.getvalue(), expected)

    def test_basic_display_name_long(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.project = 'thisIsAVeryLongprojectThatCantDisplayFully'
        mock_getTerminalSize.return_value = (self.term_width, None)
        mock_search.return_value = {self.args.project: {'summary': 'sum'}}
        expected = self.args.project + self.sep + 'sum'
        expected = expected[: (self.sum_len + self.name_len +
                               self.sep_len)] + '\n'
        pip2.cli_wrapper.search(self.args)
        self.tear_down(result.getvalue(), expected)

    def test_basic_display_sum_single_line(self, mock_search,
                                           mock_getTerminalSize):
        result = self.setup()
        self.args.project = 'pkgPlaceholder'
        mock_getTerminalSize.return_value = (self.term_width, None)
        desc = 'X' * (self.sum_len)
        mock_search.return_value = {self.args.project: {'summary': desc}}
        expected = (self.args.project + ' ' * (self.name_len -
                    len(self.args.project)) + self.sep + desc + '\n')
        pip2.cli_wrapper.search(self.args)
        self.tear_down(result.getvalue(), expected)

    def test_basic_display_sum_word_wrap(self, mock_search,
                                         mock_getTerminalSize):
        result = self.setup()
        self.args.project = 'pkgPlaceholder'
        mock_getTerminalSize.return_value = (self.term_width, None)
        desc = 'X' * int(self.sum_len * 1.5)
        mock_search.return_value = {self.args.project: {'summary': desc}}
        desc_ln1 = desc[: self.sum_len]
        desc_ln2 = desc[len(desc_ln1):]
        expected = (self.args.project + ' ' * (self.name_len -
                    len(self.args.project)) + self.sep + desc_ln1 + '\n' +
                    ' ' * (self.name_len + self.sep_len) + desc_ln2 + '\n')
        pip2.cli_wrapper.search(self.args)
        self.tear_down(result.getvalue(), expected)

    def test_basic_display_matches(self, mock_search, mock_getTerminalSize):
        result = self.setup()
        self.args.project = 'pkgPlaceholder'
        mock_getTerminalSize.return_value = (self.term_width, None)
        installed = '1.0'
        latest = '1.5'
        desc = 'X' * self.sum_len
        mock_search.return_value = {self.args.project: {'summary': desc,
                                    'installed_version': installed,
                                    'latest_version': latest}}
        expected = (self.args.project + ' ' * (self.name_len -
                    len(self.args.project)) + self.sep + desc +
                    '\n\tINSTALLED: ' + installed + '\n\tLATEST   : ' +
                    latest + '\n')
        pip2.cli_wrapper.search(self.args)
        self.tear_down(result.getvalue(), expected)

    # System level test. Runs all previous tests at different terminal sizes.
    def test_system_display_terminal_scale(self, mock_search,
                                           mock_getTerminalSize):
        # test case:
        # 35  - too small must be min of 40
        # 60  - small term
        # 180 - large term
        term_widths = [35, 60, 180]

        for term_width in term_widths:
            self.term_width = term_width
            if self.term_width >= self.min_term_width:
                width_used = self.term_width
            else:
                width_used = self.min_term_width
            self.sum_len = width_used - self.name_len - self.sep_len - 1
            self._run_all_project_tests()
            self.term_width = self.default_term_width

    def _run_all_project_tests(self):
        self.test_basic_display_no_results()
        self.test_basic_display_name_short()
        self.test_basic_display_name_long()
        self.test_basic_display_sum_single_line()
        self.test_basic_display_sum_word_wrap()
        self.test_basic_display_matches()

    def tear_down(self, result, expected):
        try:
            assert result == expected
        except AssertionError:
            result = result.replace('\n', '\\n')
            expected = expected.replace('\n', '\\n')
            output = ('\nUnit test : {0}'.format(inspect.stack()[1][3]) +
                      '\nTerm width: {0}'.format(self.term_width) +
                      '\nResult    : \n{0}\n'.format(result) +
                      '\nExpected  : \n{0}'.format(expected))
            print(output)
            raise
