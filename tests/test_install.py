import mock
import pip2.commands.install
import packaging.install
import os
import tempfile


@mock.patch.object(packaging.install, 'install')
class TestInstallAPI():

    def test_install_single_package(self, mock_func):
        mock_func.return_value = True
        expected = ['test_package1']
        result = pip2.commands.install.install(expected)

        assert result['installed'] == expected
        assert result['failed'] == []

    def test_install_multiple_packages(self, mock_func):
        mock_func.return_value = True
        expected = ['test_package1', 'test_package2', 'test_package3']
        result = pip2.commands.install.install(expected)

        assert result['installed'] == expected
        assert result['failed'] == []

    def test_install_fail_single_package(self, mock_func):
        mock_func.return_value = False
        expected = ['failing_package']
        result = pip2.commands.install.install(expected)

        assert result['installed'] == []
        assert result['failed'] == expected

    def test_install_fail_multiple_packages(self, mock_func):
        mock_func.return_value = False
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




@mock.patch.object(packaging.install, 'install')
class TestInstallCLI():

    def test_install_single_package(self, mock_func):
        pass

    def test_install_multiple_packages(self, mock_func):
        pass

    def test_install_fail_single_package(self, mock_func):
        pass

    def test_install_fail_multiple_packages(self, mock_func):
        pass
