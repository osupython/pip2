import inspect
import sys
from io import StringIO

import pip2.cli_wrapper
import pip2.commands.freeze
from pip2.compat import mock
from pip2.compat import packaging


@mock.patch.object(packaging.database, 'get_distributions')
class TestFreezeAPI():
    def test_basic_freeze(self, mock_gen):
        # create the distributions that the gen will return
        dis1 = mock.Mock()
        dis1.name = 'test_project1'
        dis1.version = '1.0'
        dis2 = mock.Mock()
        dis2.name = 'test_project2'
        dis2.version = '2.0'
        dis3 = mock.Mock()
        dis3.name = 'test_project3'
        dis3.version = '3.0'

        # get_distributions gen returns a iterator over distributions objects
        mock_gen.return_value = iter([dis1, dis2, dis3])
        expected = {'test_project1': {'version': '1.0'}, 'test_project2':
                    {'version': '2.0'}, 'test_project3': {'version': '3.0'}}
        # run the command
        result = pip2.commands.freeze.freeze()
        try:
            assert result == expected
        except AssertionError:
            print('result  : {0}'.format(result))
            print('expected: {0}'.format(expected))
            raise


@mock.patch.object(pip2.commands.freeze, 'freeze')
class TestFreezeCLI():
    originalOut = sys.stdout

    #capture stdout
    def setup(self):
        sys.stdout = result = StringIO()
        return result

    def test_basic_freeze(self, mock_func):
        args = mock.Mock()
        result = self.setup()
        mock_func.return_value = {'test_project1': {'version': '1.0'},
                                  'test_project2': {'version': '2.0'},
                                  'test_project3': {'version': '3.0'}}
        pip2.cli_wrapper.freeze(args)
        expected = 'test_project1==1.0\ntest_project2==2.0\n' + \
                   'test_project3==3.0\n'
        self.tear_down(result.getvalue(), expected)

    def tear_down(self, result, expected):
        try:
            assert result == expected
        except AssertionError:
            # display newlines for easier comparison
            result = result.replace('\n', '\\n')
            expected = expected.replace('\n', '\\n')
            output = ('\n\nTEST FAILED' +
                      '\nFunction: {0}'.format(inspect.stack()[1][3]) +
                      '\nResult  : {0}\n'.format(result) +
                      '\nExpected: {0}'.format(expected))
            print(output, file=sys.stderr)
            raise
        finally:
            sys.stdout = self.originalOut
