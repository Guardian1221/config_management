import struct
import sys
import xml.etree.ElementTree as ET

# Функция для интерпретации инструкций
def interpret(binary_file, result_file, mem_start, mem_end):
    with open(binary_file, 'rb') as bin_file:
        memory = [0] * 100  # Инициализация памяти (100 ячеек)

        while True:
            instruction = bin_file.read(7)
            if len(instruction) < 7:
                break

            opcode, arg1, arg2 = struct.unpack('<IBH', instruction)

            if opcode == (26 << 3) | 0x1:  # LOAD
                memory[arg1] = arg2
            elif opcode == (26 << 3) | 0x2:  # READ
                memory[arg1] = arg2
            elif opcode == (26 << 3) | 0x3:  # WRITE
                memory[arg1] = arg2
            elif opcode == (26 << 3) | 0x4:  # XOR
                memory[arg1] ^= arg2
            else:
                raise ValueError(f"Unknown opcode: {opcode}")

        # Запись состояния памяти в XML файл
        root = ET.Element("memory")
        for i in range(mem_start, mem_end):
            cell = ET.SubElement(root, "cell", address=str(i))
            cell.text = str(memory[i])

        tree = ET.ElementTree(root)
        tree.write(result_file)

if __name__ == "__main__":
    binary_file = sys.argv[1]
    result_file = sys.argv[2]
    mem_start = int(sys.argv[3])
    mem_end = int(sys.argv[4])

    interpret(binary_file, result_file, mem_start, mem_end)
