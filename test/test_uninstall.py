import unittest
import pip2.commands.uninstall
import mock

class UninstallTest(unittest.TestCase):

    @mock.patch.object(pip2.commands.uninstall, 'command')
    def test_uninstall_result(self, mock_command):
        pip2.commands.uninstall.command.return_value = True
        result = pip2.commands.uninstall.uninstall("test_package")
        self.assertEqual(result, True)

        pip2.commands.uninstall.command.return_value = True
        result = pip2.commands.uninstall.uninstall("test_package")

