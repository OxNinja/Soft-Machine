# Soft Machine

Python custom virtual machine.

## Features

* [ ] Registers
    * [x] Basic registers
    * [ ] Flags
        * [ ] Zero flag 
* [ ] Stack
    * [ ] LIFO
    * [ ] Max size 
    * [ ] Stackframes
* [ ] Heap
    * [ ] Max size
* [ ] Instructions
    * [x] `add reg, val`
    * [x] `add reg, reg`
    * [ ] `sub reg, val`
    * [ ] `sub reg, reg`
    * [ ] `cmp reg, val`
    * [ ] `cmp reg, reg`
    * [x] `mov reg, val`
    * [x] `mov reg, reg`
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
* [x] Exec instructions
    * [x] From file
    * [x] From stdin

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
