import os
import json
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime

class Emulator:
    def __init__(self, config_path):
        self.load_config(config_path)
        self.current_directory = '/'
        self.commands = {
            'ls': self.list_directory,
            'cd': self.change_directory,
            'exit': self.exit_emulator,
            'head': self.head,
            'whoami': self.whoami
        }
        self.load_virtual_filesystem()
        self.run_startup_script()

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
            self.username = config['username']
            self.vfs_path = config['vfs_path']
            self.log_path = config['log_path']
            self.startup_script = config['startup_script']

    def load_virtual_filesystem(self):
        self.vfs_root = '/tmp/vfs'
        if not os.path.exists(self.vfs_root):
            os.makedirs(self.vfs_root)
        with zipfile.ZipFile(self.vfs_path, 'r') as zip_ref:
            zip_ref.extractall(self.vfs_root)

    def log_action(self, action):
        root = ET.Element("log")
        entry = ET.SubElement(root, "entry")
        entry.set("user", self.username)
        entry.set("action", action)
        entry.set("timestamp", datetime.now().isoformat())
        
        tree = ET.ElementTree(root)
        with open(self.log_path, 'wb') as log_file:
            tree.write(log_file)

    def run_startup_script(self):
        if os.path.exists(self.startup_script):
            with open(self.startup_script, 'r') as file:
                for line in file:
                    self.execute_command(line.strip())

    def execute_command(self, command):
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd in self.commands:
            self.commands[cmd](*args)
        else:
            print(f"{cmd}: command not found")

    def list_directory(self):
        print(os.listdir(self.vfs_root + self.current_directory))
        self.log_action("ls")

    def change_directory(self, path):
        new_path = os.path.join(self.vfs_root, self.current_directory, path)
        if os.path.isdir(new_path):
            self.current_directory = os.path.join(self.current_directory, path)
            self.log_action(f"cd {path}")
        else:
            print(f"cd: no such file or directory: {path}")

    def exit_emulator(self):
        self.log_action("exit")
        exit(0)

    def head(self, filename):
        file_path = os.path.join(self.vfs_root, self.current_directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                for _ in range(10):
                    line = file.readline()
                    if not line:
                        break
                    print(line.strip())
            self.log_action(f"head {filename}")
        else:
            print(f"head: {filename}: No such file")

    def whoami(self):
        print(self.username)
        self.log_action("whoami")

if __name__ == "__main__":
    emulator = Emulator('config.json')
    while True:
        command = input(f"{emulator.username}@emulator:{emulator.current_directory}$ ")
        emulator.execute_command(command)