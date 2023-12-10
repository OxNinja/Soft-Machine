# Soft Machine

Python custom virtual machine.

## Features

* [ ] Registers
    * [ ] Basic registers
    * [ ] Flags
        * [x] Zero flag 
* [ ] Stack
    * [ ] LIFO
    * [ ] Max size 
    * [ ] Stackframes
* [ ] Heap
    * [ ] Max size
* [ ] Instructions
    * [ ] `add reg, val`
    * [ ] `add reg, reg`
    * [ ] `sub reg, val`
    * [ ] `sub reg, reg`
    * [ ] `cmp reg, val`
    * [ ] `cmp reg, reg`
    * [ ] `mov reg, val`
    * [ ] `mov reg, reg`
    * [ ] `push val`
    * [ ] `push reg`
    * [ ] `pop reg`
    * [ ] `jmp addr`
    * [ ] `jmp label`
    * [ ] `call func`
    * [ ] `exit`
* [ ] Assemble code
    * [ ] From file
    * [ ] From stdin
* [ ] Disassemble code
    * [ ] From file
    * [ ] From stdin
* [ ] Exec instructions
    * [ ] From file
    * [ ] From stdin

## Install

```sh 
# Get sources
git clone ...
cd Soft-Machine

# Use a virtual environment
python3 -m venv my-venv
source my-venv/bin/activate

# Install via pip
pip install -e .
```

## Use

```sh
soft-machine exec --file code.txt
soft-machine assemble --stdin "mov a, 11; mov b, 0x45; exit"
soft-machine disassemble --file code.bin
```