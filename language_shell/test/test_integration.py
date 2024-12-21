import pytest
from config_tool.parser import parse_yaml
from config_tool.generator import generate_config

def test_integration_simple():
    yaml_input = """
    key1: value1
    key2: 42
    """
    expected_output = "@{\n key1 = 'value1';\n key2 = 42;\n}"
    data = parse_yaml(yaml_input)
    assert generate_config(data) == expected_output

def test_integration_complex():
    yaml_input = """
    settings:
      debug: true
      levels:
        - info
        - warn
        - error
    """
    expected_output = (
        "@{\n"
        " settings = @{\n"
        "  debug = true;\n"
        "  levels = [ 'info' 'warn' 'error' ];\n"
        " };\n"
        "}"
    )
    data = parse_yaml(yaml_input)
    assert generate_config(data) == expected_output
