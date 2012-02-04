import unittest
import pip2.commands.install
import mock

class InstallTest(unittest.TestCase):
    
    @mock.patch.object(pip2.commands.install, 'command')
    def test_install_result(self, mock_command):
        pip2.commands.install.command.return_value = True
        result = pip2.commands.install.install("test_package")
        self.assertEqual(result, True)

        pip2.commands.install.command.return_value = False
        result = pip2.commands.install.install("test_package")
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()


