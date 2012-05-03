import mock
import pip2.commands.install
import packaging.install
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
    def test_local_project(self, mock_local, mock_install):
        file1 = tempfile.NamedTemporaryFile()
        file2 = "#"
        mock_local.return_value = True
        mock_install.return_value = True

        pip2.commands.install.install(file1.name)
        assert mock_local.called == True
        pip2.commands.install.install(file2)
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
