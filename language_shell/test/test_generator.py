import pytest
from config_tool.generator import generate_config

def test_generate_from_dict():
    data = {"key1": "value1", "key2": 42}
    expected_output = "@{\n key1 = 'value1';\n key2 = 42;\n}"
    assert generate_config(data) == expected_output

def test_generate_from_list():
    data = ["item1", "item2"]
    expected_output = "[ 'item1' 'item2' ]"
    assert generate_config(data) == expected_output

def test_generate_nested():
    data = {"key1": {"nested_key": "nested_value"}}
    expected_output = "@{\n key1 = @{\n  nested_key = 'nested_value';\n };\n}"
    assert generate_config(data) == expected_output
