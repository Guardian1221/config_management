import unittest
from emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = ShellEmulator("config.json")

    def test_ls(self):
        expected_files = ['file1.txt', 'file2.txt']
        with self.assertLogs('emulator', level='INFO') as log:
            self.emulator.ls()
            self.assertIn('INFO:emulator:ls', log.output)

    def test_cd(self):
        self.emulator.cd('some_directory')
        self.assertEqual(self.emulator.current_directory, 'some_directory')

    def test_whoami(self):
        with self.assertLogs('emulator', level='INFO') as log:
            self.emulator.whoami()
            self.assertIn('INFO:emulator:user', log.output)

    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.emulator.exit()

if __name__ == "__main__":
    unittest.main()

