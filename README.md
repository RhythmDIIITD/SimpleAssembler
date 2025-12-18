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

