import unittest
from emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        # Предположим, что у вас есть конфигурационный файл config.json
        self.emulator = ShellEmulator("config.json")

    def test_ls(self):
        # Проверка вывода команды ls
        expected_files = ['file1.txt', 'file2.txt']  # Замените на ожидаемые файлы
        with self.assertLogs('emulator', level='INFO') as log:
            self.emulator.ls()
            self.assertIn('INFO:emulator:ls', log.output)

    def test_cd(self):
        # Проверка корректности выполнения команды cd
        self.emulator.cd('some_directory')
        self.assertEqual(self.emulator.current_directory, 'some_directory')

    def test_whoami(self):
        # Проверка вывода команды whoami
        with self.assertLogs('emulator', level='INFO') as log:
            self.emulator.whoami()
            self.assertIn('INFO:emulator:user', log.output)

    def test_exit(self):
        # Проверка корректности выхода из эмулятора
        with self.assertRaises(SystemExit):
            self.emulator.exit()

if __name__ == "__main__":
    unittest.main()

