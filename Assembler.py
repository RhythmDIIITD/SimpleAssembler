def readfile(file_path):
    list = []
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().replace(",", " ").split()
            list.append(words)
    
    return list

def labelmaker(list):
    labels = {}
    pc = 0
    for i in range(0,len(list)):
        if ":" in list[i][0]:
            labels[list[i][0]] = pc
        pc = pc+1

    return labels

Dictionary_of_instruction = {
    "R-type": {
        "add": {"func7": "0000000", "func3": "000", "opcode": "0110011"},
        "sub": {"func7": "0100000", "func3": "000", "opcode": "0110011"},
        "slt": {"func7": "0000000", "func3": "010", "opcode": "0110011"},
        "srl": {"func7": "0000000", "func3": "101", "opcode": "0110011"},
        "or": {"func7": "0000000", "func3": "110", "opcode": "0110011"},
        "and": {"func7": "0000000", "func3": "111", "opcode": "0110011"}
    },
    "I-type": {
        "addi": {"func3": "000", "opcode": "0010011"},
        "slti": {"func3": "010", "opcode": "0010011"},
        "ori": {"func3": "110", "opcode": "0010011"},
        "andi": {"func3": "111", "opcode": "0010011"},
        "lb": {"func3": "000", "opcode": "0000011"},
        "lh": {"func3": "001", "opcode": "0000011"},
        "lw": {"func3": "010", "opcode": "0000011"}
    },
    "S-type": {
        "sb": {"func3": "000", "opcode": "0100011"},
        "sh": {"func3": "001", "opcode": "0100011"},
        "sw": {"func3": "010", "opcode": "0100011"}
    },
    "B-type": {
        "beq": {"func3": "000", "opcode": "1100011"},
        "bne": {"func3": "001", "opcode": "1100011"},
        "blt": {"func3": "100", "opcode": "1100011"},
        "bge": {"func3": "101", "opcode": "1100011"}
    },
    "J-type": {
        "jal": {"opcode": "1101111"}
    }
}

Register_dictionary = {
    "x0": "00000", "zero": "00000",
    "x1": "00001", "ra": "00001",
    "x2": "00010", "sp": "00010",
    "x3": "00011", "gp": "00011",
    "x4": "00100", "tp": "00100",
    "x5": "00101", "t0": "00101",
    "x6": "00110", "t1": "00110",
    "x7": "00111", "t2": "00111",
    "x8": "01000", "s0": "01000",
    "x9": "01001", "s1": "01001",
    "x10": "01010", "a0": "01010",
    "x11": "01011", "a1": "01011",
    "x12": "01100", "a2": "01100",
    "x13": "01101", "a3": "01101",
    "x14": "01110", "a4": "01110",
    "x15": "01111", "a5": "01111",
    "x16": "10000", "a6": "10000",
    "x17": "10001", "a7": "10001",
    "x18": "10010", "s2": "10010",
    "x19": "10011", "s3": "10011",
    "x20": "10100", "s4": "10100",
    "x21": "10101", "s5": "10101",
    "x22": "10110", "s6": "10110",
    "x23": "10111", "s7": "10111",
    "x24": "11000", "s8": "11000",
    "x25": "11001", "s9": "11001",
    "x26": "11010", "s10": "11010",
    "x27": "11011", "s11": "11011",
    "x28": "11100", "t3": "11100",
    "x29": "11101", "t4": "11101",
    "x30": "11110", "t5": "11110",
    "x31": "11111", "t6": "11111"
}





file_path = "Ex_test_6.txt"
list = readfile("Ex_test_6.txt")
labels = labelmaker(list)
print(list)
print(labels)

