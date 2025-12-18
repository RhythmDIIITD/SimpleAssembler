# Simple RISC-V Assembler

A Python-based assembler for the **RISC-V 32-bit Instruction Set Architecture (ISA)**.  
This assembler reads an assembly program as an input text file and generates the corresponding binary instructions as an output text file. It also performs syntax and semantic checks, providing error notifications with line numbers when necessary.

---

## Features

- Converts **RISC-V 32-bit assembly instructions** into **32-bit binary instructions**.
- Supports labels for **branch and jump instructions**.
- Handles **empty lines, instructions, and labels** correctly.
- Performs **error detection** including:
  - Typos in instruction or register names.
  - Illegal immediate values (out of bounds).
  - Missing Virtual Halt instruction.
  - Virtual Halt not being the last instruction.
- Generates a binary output file when code is error-free.
- Provides **error notifications** (stdout) with line numbers for any invalid instructions.
- Includes **10 test cases** with expected outputs for validation.

## Project Structure
Run the assembler:

python assembler.py <input_assembly_file> <output_binary_file>


<input_assembly_file> → Path to the input .asm file

<output_binary_file> → Path for saving the output .bin file

Example:

python assembler.py test_cases/test1.asm output/test1.bin
Instruction Encoding Examples
R-type
add s1,s2,s3
[31:25] [24:20] [19:15] [14:12] [11:7] [6:0]
0000000 10011 10010 000 01001 0110011

I-type
jalr ra,a5,-07
[31:20] [19:15] [14:12] [11:7] [6:0]
111111111001 01111 000 00001 1100111

lw a5,20(s1)
[31:20] [19:15] [14:12] [11:7] [6:0]
000000010100 01001 010 01110 0000011

S-type
sw ra,32(sp)
[31:25] [24:20] [19:15] [14:12] [11:7] [6:0]
0000001 00001 00010 010 00000 0100011

B-type
blt a4,a5,label
immediate = 200 (binary: 0000 0000 1100 1000)
[31:25] [24:20] [19:15] [14:12] [11:7] [6:0]
0000110 01111 01110 100 01000 1100011

U-type
auipc s2,-30
[31:12] [11:7] [6:0]
11111111111111111111 10010 0010111

J-type
jal ra,label
immediate = -1024 (binary: 1111 1111 1100 0000 0000)
[31:12] [11:7] [6:0]
11000000000111111111 00001 1101111

Memory Layout

Program Memory: 256 bytes (64 × 32-bit instructions), addresses 0x0000_0000 → 0x0000_00FF

Stack Memory: 128 bytes (32 × 32-bit registers), grows downwards, addresses 0x0000_0100 → 0x0000_017F

Data Memory: 128 bytes (32 × 32-bit words), using first 32 locations, addresses 0x0001_0000 → 0x0001_007F
