import pytest
from config_tool.parser import parse_yaml

def test_parse_valid_yaml():
    yaml_input = """
    key1: value1
    key2: 42
    key3:
      - item1
      - item2
    """
    expected_output = {
        "key1": "value1",
        "key2": 42,
        "key3": ["item1", "item2"]
    }
    assert parse_yaml(yaml_input) == expected_output

def test_parse_invalid_yaml():
    yaml_input = """
    key1: value1
    key2: [item1, item2
    """
    with pytest.raises(ValueError):
        parse_yaml(yaml_input)
