import os

import pip2.commands.install
from pip2.compat import mock
from pip2.compat import packaging


@mock.patch.object(packaging.install, 'install')
class TestInstallAPI():

    def test_install_single_package(self, mock_install):
        mock_install.return_value = True
        expected = ['test_package1']
        result = pip2.commands.install.install(expected)

        assert result['installed'] == expected
        assert result['failed'] == []

    def test_install_multiple_packages(self, mock_install):
        mock_install.return_value = True
        expected = ['test_package1', 'test_package2', 'test_package3']
        result = pip2.commands.install.install(expected)

        assert result['installed'] == expected
        assert result['failed'] == []

    def test_install_fail_single_package(self, mock_install):
        mock_install.return_value = False
        expected = ['failing_package']
        result = pip2.commands.install.install(expected)

        assert result['installed'] == []
        assert result['failed'] == expected

    def test_install_fail_multiple_packages(self, mock_install):
        mock_install.return_value = False
        expected = ['test_package1', 'test_package2']
        result = pip2.commands.install.install(expected)

        assert result['installed'] == []
        assert result['failed'] == expected

    @mock.patch.object(packaging.install, 'install_local_project')
    @mock.patch.object(os.path, 'exists')
    def test_local_project(self, mock_os, mock_local, mock_install):
        mock_local.return_value = True
        mock_install.return_value = True

        mock_os.return_value = True
        pip2.commands.install.install("test")
        assert mock_local.called == True

        mock_os.return_value = False
        pip2.commands.install.install("test")
        assert mock_install.called == True

    def test_install_mixed_results(self, mock_install):
        # The current expected behavior is to allow some packages to be
        # installed even if there other packages fail to install.  In the
        # future, it will probably be all or nothing.  See issue #51 for more
        # details.

        returns = [True, False]
        mock_install.side_effect = lambda *args: returns.pop(0)
        successes = ['a-real-package']
        failures = ['not-a-package']
        result = pip2.commands.install.install(successes + failures)

        assert result['installed'] == successes
        assert result['failed'] == failures


@mock.patch.object(packaging.install, 'install')
class TestInstallCLI():

    def test_install_single_package(self, mock_func):
        pass

    def test_install_multiple_packages(self, mock_install):
        pass

    def test_install_fail_single_package(self, mock_install):
        pass

    def test_install_fail_multiple_packages(self, mock_install):
        pass
