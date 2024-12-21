import subprocess

def test_interpreter():
    subprocess.run(["python3", "../interpreter/interpreter.py"], check=True)
    with open("../interpreter/result.xml", "r") as result:
        content = result.read()
        assert "<address>0</address>" in content
        assert "<value>123</value>" in content

if __name__ == "__main__":
    test_interpreter()