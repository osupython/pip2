"""
Mock testing for uninstall command.
"""

import pip2.commands.uninstall
from pip2.compat import mock
from pip2.compat import packaging


@mock.patch.object(packaging.install, 'remove')
class TestUninstallAPI():

    def test_uninstall_single_package(self, mock_func):
        mock_func.return_value = True
        expected = ['test_package1']
        result = pip2.commands.uninstall.uninstall(expected)

        assert result['uninstalled'] == expected
        assert result['failed'] == []

    def test_uninstall_multiple_packages(self, mock_func):
        mock_func.return_value = True
        expected = ['test_package1', 'test_package2', 'test_package3']
        result = pip2.commands.uninstall.uninstall(expected)

        assert result['uninstalled'] == expected
        assert result['failed'] == []

    def test_uninstall_fail_single_package(self, mock_func):
        mock_func.return_value = False
        expected = ['failing_package1']
        result = pip2.commands.uninstall.uninstall(expected)

        assert result['uninstalled'] == []
        assert result['failed'] == expected

    def test_uninstall_fail_multiple_packages(self, mock_func):
        mock_func.return_value = False
        expected = ['failing_package1', 'failing_package2']
        result = pip2.commands.uninstall.uninstall(expected)

        assert result['uninstalled'] == []
        assert result['failed'] == expected


@mock.patch.object(packaging.install, 'remove')
class TestUninstallCLI():

    def test_uninstall_single_package(self, mock_func):
        pass

    def test_uninstall_multiple_packages(self, mock_func):
        pass

    def test_uninstall_fail_single_package(self, mock_func):
        pass

    def test_uninstall_fail_multiple_packages(self, mock_func):
        pass
