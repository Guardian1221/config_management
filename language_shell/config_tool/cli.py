import sys
import argparse
from parser import parse_yaml
from generator import generate_config
import yaml

def load_input_data():
    with open("input.yaml") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Path to the input YAML file')
    parser.add_argument('output_file', help='Path to the output file')
    args = parser.parse_args()

    # Читаем входные данные из YAML файла
    with open(args.input_file, 'r') as file:
        input_data = yaml.safe_load(file)

    print(f'Входные данные: {input_data}')
    print(f'Собираемся записать результат в файл: {args.output_file}')
    
    # Здесь добавьте логику обработки данных и записи в выходной файл
    # Например:
    with open(args.output_file, 'w') as file:
        file.write(str(input_data))  # Пример записи данных

if __name__ == '__main__':
    main()

