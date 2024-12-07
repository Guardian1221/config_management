import configparser
import subprocess
import sys
import json

class DependencyVisualizer:

    
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        # Проверка наличия необходимых параметров
        if 'settings' not in self.config:
            raise ValueError("Отсутствует секция [settings] в конфигурационном файле.")
        
        self.output_file = self.config['settings'].get('output_file', None)

        if not self.output_file:
            raise ValueError("Параметр output_file должен быть указан в конфигурационном файле.")

    def get_dependencies(self, package_name):
    # Укажите полный путь к npm
        npm_path = r'C:\Program Files\nodejs\npm.cmd'  # Убедитесь, что это правильный путь
        result = subprocess.run([npm_path, 'view', package_name, 'dependencies', '--json'], stdout=subprocess.PIPE)
        dependencies = json.loads(result.stdout)
        return dependencies


    def build_graph(self, dependencies, package_name):
        graph = "@startuml\n"
        for package, version in dependencies.items():
            graph += f'"{package}" --> "{package_name}"\n'
        graph += "@enduml"
        return graph

    def save_graph(self, graph):
        with open(self.output_file, 'w') as f:
            f.write(graph)

    def visualize(self, package_name):
        dependencies = self.get_dependencies(package_name)
        graph = self.build_graph(dependencies, package_name)
        self.save_graph(graph)
        print(graph)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python visualizer.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    visualizer = DependencyVisualizer(config_file)

    # Запрашиваем имя пакета у пользователя
    package_name = input("Введите имя анализируемого пакета: ")
    visualizer.visualize(package_name)
