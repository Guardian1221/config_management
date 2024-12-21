import subprocess

def test_assembler():
    subprocess.run(["python3", "../assembler/assembler.py"], check=True)
    with open("../assembler/program_log.xml", "r") as log:
        content = log.read()
        assert "<opcode>LOAD</opcode>" in content
        assert "<arg1>335</arg1>" in content

if __name__ == "__main__":
    test_assembler()