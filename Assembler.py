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

Dictionary_of_instruction = {"R-type":["add","sub","slt","srl","or","and"], 
                             "I-type":["lw","addi","jalr"],
                             "S-type":["sw"],
                             "B-type":["beq","bne"],
                             "J-type":["jal"]}

file_path = "Ex_test_6.txt"
list = readfile("Ex_test_6.txt")
labels = labelmaker(list)
print(list)
print(labels)

