import yaml
def parse_yaml(input_data):
    print("Пытаемся парсить YAML...")
    try:
        data = yaml.safe_load(input_data)
        print("YAML успешно разобран:", data)
        return data
    except yaml.YAMLError as e:
        raise ValueError(f"Ошибка при парсинге YAML: {e}")

