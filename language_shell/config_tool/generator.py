def generate_config(data):
    print("Пытаемся сгенерировать конфигурацию из:", data)
    if isinstance(data, dict):
        result = ["@{"]
        for key, value in data.items():
            result.append(f" {key} = {generate_config(value)};")
        result.append("}")
        return "\n".join(result)
    elif isinstance(data, list):
        values = " ".join(generate_config(v) for v in data)
        return f"[ {values} ]"
    elif isinstance(data, str):
        return f"'{data}'"
    elif isinstance(data, (int, float)):
        return str(data)
    else:
        raise ValueError(f"Неподдерживаемый тип данных: {type(data)}")

