import struct

# Функция для кодирования инструкции
def encode_instruction(opcode, args):
    if opcode == 'LOAD':
        return struct.pack('<IBH', (26 << 3) | 0x1, args[0], args[1])  # Пример для LOAD
    elif opcode == 'READ':
        return struct.pack('<IBH', (26 << 3) | 0x2, args[0], args[1])  # Пример для READ
    elif opcode == 'WRITE':
        return struct.pack('<IBH', (26 << 3) | 0x3, args[0], args[1])  # Пример для WRITE
    elif opcode == 'XOR':
        return struct.pack('<IBH', (26 << 3) | 0x4, args[0], args[1])  # Пример для XOR
    else:
        raise ValueError(f"Unknown opcode: {opcode}")

# Функция для ассемблирования программы из текстового файла
def assemble(input_file, output_bin_file, output_log_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    binary_instructions = []
    for line in lines:
        parts = line.strip().split()
        opcode = parts[0]
        
        args = [int(arg.strip('R,')) for arg in parts[1:]]
        binary = encode_instruction(opcode, args)
        binary_instructions.append(binary)

    with open(output_bin_file, 'wb') as bin_file:
        for instruction in binary_instructions:
            bin_file.write(instruction)

    # Логирование инструкций
    with open(output_log_file, 'w') as log_file:
        log_file.write('<instructions>\n')
        for line in lines:
            parts = line.strip().split()
            opcode = parts[0]
            args = parts[1:]
            log_file.write(f"<instruction><opcode>{opcode}</opcode><arg1>{args[0]}</arg1><arg2>{args[1]}</arg2></instruction>\n")
        log_file.write('</instructions>')

if __name__ == "__main__":
    assemble("assempler/test_program.asm", "assempler/program.bin", "assempler/program_log.xml")
